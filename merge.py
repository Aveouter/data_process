# coding=utf-8
import os
import numpy as np
from data_class_define import base, BMI, CRRT, gcs, sofa, coagulation, LFTs, Ventilator, MV, UO, Biochemistry, Vitalsigns, CBC, Vasoactive, ABG, sick
from data_reader import data_loader,timestamp_to_ruby_time_str,sex_to_int,load_excel,fields_map
import pandas as pd
import datetime
import xlsxwriter


def merge_patient_data(primary_list, data_dict):
    list_sick = []
    index_map = {key: 0 for key in data_dict}
    for primary in primary_list:
        if not primary.time_CRRT:  # So unsure
            continue
        s = sick()
        # get the CRRT
        s.id = getattr(primary, 'id', '')
        s.starttime = getattr(primary, 'starttime', '')
        s.step = getattr(primary, 'step', '')
        s.action = getattr(primary, 'action', '')
        s.time_CRRT = getattr(primary, 'time_CRRT', '')
        s.time_IRRT = getattr(primary, 'time_IRRT', '')
        list_sick.append(s)

        ## define time and step
        std_time = 0
        first_step = 0
        for key, data_list in data_dict.items():
            idx = index_map[key]
            # define a list temp_list = []
            exclude_keys = {'id', 'starttime', 'step', 'action', 'time_CRRT', 'time_IRRT'}
            temp_list = {key: 0 for key in vars(s) if key not in exclude_keys}
            while idx < len(data_list):
                item = data_list[idx]
                cur_step = int((item.starttime - std_time) * 24 // 4 - first_step)    ## 这一步到底怎么做std_time and first_step is what
                if item.id < primary.id or (item.id == primary.id and cur_step < primary.step):
                    idx += 1
                elif item.id == primary.id and cur_step == primary.step:
                    ## 这里的逻辑很复杂，连续和离散变量的处理，这里目前就break掉，但是如果是真实情况需要一个temp_list存,分情况处理，建议封装
                    for attr_sick, attr_item in fields_map[key].items():
                        setattr(s, attr_sick, getattr(item, attr_item))
                    idx += 1
                    break
                else:
                    break
            index_map[key] = idx

    return list_sick

def sick_creator(lists, save_path) -> None:
    list_sick = merge_patient_data(lists.pop('CRRT', None), lists)
    if not list_sick:
        return
    field_names = [attr for attr in vars(list_sick[0]) if not attr.startswith('_') and not callable(getattr(list_sick[0], attr))]
    save_path = os.path.join(os.path.dirname(__file__), "data/total.xlsx"); os.makedirs(os.path.dirname(save_path), exist_ok=True)
    workbook = xlsxwriter.Workbook(save_path)
    worksheet = workbook.add_worksheet()
    worksheet.write_row(0, 0, field_names)
    for i, s in enumerate(list_sick):
        row = [getattr(s, field, '') for field in field_names]
        worksheet.write_row(i + 1, 0, row)
    workbook.close()
    print(f'saved as xlsx @{save_path}.')

def main():
    data_frames = data_loader()
    #load data
    list_base = load_excel(data_frames['base'],'base',fields_map['base']) # over check warning hospital! warning id!#id = hadm? 
    list_BMI = load_excel(data_frames['BMI'],'BMI',fields_map['BMI']) # over check warning id!#id = hadm? 
    list_CRRT = load_excel(data_frames['CRRT'],'CRRT',fields_map['CRRT'])# over check just id  ,starttime maybe error, i have to except cause the time is type float.
    list_gcs = load_excel(data_frames['gcs'],'gcs',fields_map['gcs'])#id = hadm, NO starttime.is charttime?
    list_sofa = load_excel(data_frames['sofa'],'sofa',fields_map['sofa'])#id = hadm?
    list_coagulation = load_excel(data_frames['coagulation'],'coagulation',fields_map['coagulation'])
    list_LFTs = load_excel(data_frames['LFTs'],'LFTs',fields_map['LFTs'])
    list_Ventilator = load_excel(data_frames['Ventilator'],'Ventilator',fields_map['Ventilator'])
    list_MV = load_excel(data_frames['MV'],'MV',fields_map['MV'])
    list_UO = load_excel(data_frames['UO'],'UO',fields_map['UO'])
    list_Biochemistry = load_excel(data_frames['Biochemistry'],'Biochemistry',fields_map['Biochemistry'])
    list_Vitalsigns = load_excel(data_frames['Vitalsigns'],'Vitalsigns',fields_map['Vitalsigns'])
    list_CBC = load_excel(data_frames['CBC'],'CBC', fields_map['CBC'])
    list_Vasoactive = load_excel(data_frames['Vasoactive'],'Vasoactive', fields_map['Vasoactive'])
    list_ABG = load_excel(data_frames['ABG'],'ABG', fields_map['ABG'])

    list_dict = {
        'base': list_base,'BMI': list_BMI,'CRRT': list_CRRT,'gcs': list_gcs,'sofa': list_sofa,
        'coagulation': list_coagulation,'LFTs': list_LFTs,'Ventilator': list_Ventilator,'MV': list_MV,
        'UO': list_UO,'Biochemistry': list_Biochemistry,'Vitalsigns': list_Vitalsigns,'CBC': list_CBC,
        'Vasoactive': list_Vasoactive,'ABG': list_ABG
    }

    sick_creator(list_dict,'data/total.xlsx')

if __name__ == "__main__":
    main()