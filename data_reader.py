import datetime
import os
import pandas as pd
from data_class_define import base, BMI, CRRT, gcs, sofa, coagulation, LFTs, Ventilator, MV, UO, Biochemistry, Vitalsigns, CBC, Vasoactive, ABG, sick


def sex_to_int(val):
    if val == "M":
        return 0
    elif val == 'F':
        return 1
    else:
        print(f'sex:{val}')
        return None  # 或者其他默认值

def timestamp_to_ruby_time_str(ts):
    """
    将 pandas Timestamp 或 datetime 转换为 Ruby 风格的时间字符串
    如果不是时间类型，返回原值
    """
    if not isinstance(ts, (pd.Timestamp, datetime.datetime)):
        return ts 
    if ts.tzinfo is None:
        ts = ts.tz_localize('Asia/Shanghai')  # 根据需要换成你的时区
    
    tz_str = ts.strftime('%z')
    return ts.strftime(f'%Y-%m-%d %H:%M:%S {tz_str}')


def data_loader():
    # 定义路径字典
    base_dir = os.path.dirname(__file__)
    paths = {
        'base': 'data/RRT基本信息.xlsx',
        'BMI': 'data/BMI.xlsx',
        'CRRT': 'data/new_state.xlsx',
        'gcs': 'data/gcs.xlsx',
        'sofa': 'data/SOFA.xlsx',
        'coagulation': 'data/凝血.xlsx',
        'LFTs': 'data/肝功.xlsx',
        'Ventilator': 'data/呼吸机参数.xlsx',
        'MV': 'data/机械通气.xlsx',
        'UO': 'data/尿量及速率.xlsx',
        'Biochemistry': 'data/生化.xlsx',
        'Vitalsigns': 'data/生命体征.xlsx',
        'CBC': 'data/血常规.xlsx',
        'Vasoactive': 'data/血管活性药物.xlsx',
        'ABG': 'data/血气.xlsx'
    }
    # 批量读取所有表格
    data_frames = {}
    for name, path in paths.items():
        try:
            path = os.path.join(base_dir,path)
            df = pd.read_excel(path, engine='openpyxl', nrows=20)
            data_frames[name] = df
        except Exception as e:
            print(f"❌ 读取失败: {name} → 错误: {e}")
    print("\n📊 已成功读取表格:")
    print(" | ".join([f"{name}: {df.shape}" for name, df in data_frames.items()]))
    return data_frames

fields_map = {
    'base': {"id": 1, "age": 3, "sex": 4, "deathtime": 8, "hospital": 9} ,# over check warning hospital! warning id!#id = hadm? 
    'BMI': {"id": 1, "charttime": 3, "starttime": 4, "weight": 6, "height": 7}, # over check warning id!#id = hadm? 
    'CRRT':{"id": 0, "starttime": 1, "step": 2, "action": 3, "time_CRRT": 4, "time_IRRT": 5},# over check just id  ,starttime maybe error, i have to except cause the time is type float.
    'gcs':{"id": 1, "starttime": 3, "gcs": 5},#id = hadm, NO starttime.is charttime?
    'sofa': {"id": 0, "starttime": 3, "sofa": 5},#id = hadm?
    'coagulation': {"id": 1, "charttime": 3, "inr": 5, "pt": 6, "ptt": 7},#id = hadm?
    'LFTs':{"id": 1, "charttime": 3, "alt": 5, "ast": 6, "bilirubin": 7},
    'Ventilator': {"id": 1, "charttime": 4, "respiratory_rate_set": 5,  #id = hadm? 
                    "respiratory_rate_total": 6, "respiratory_rate_spontaneous": 7,
                    "minute_volume": 8, "tidal_volume_set": 9, 
                    "tidal_volume_spontaneous": 11, "plateau_pressure": 12,
                    "peep": 13, "fio2": 14},
    'MV' : {"id": 1, "starttime": 3, "ventilation_status": 5},#id = hadm? 
    'UO' : {"id": 1, "chartttime": 3, "uo_12": 7, "uo_24": 8},#id = hadm? 
    'Biochemistry': {"id": 1, "charttime": 3, "albumin": 5, "bicarbonate": 6, 
                    "bun": 7,"calcium": 8, "chloride": 9, "creatinine": 10, 
                    "glucose": 11,"sodium": 12, "potassium": 13, "magnesium": 14},
    'Vitalsigns' :{"id": 1, "charttime": 3, "heart_rate": 4, "sbp": 5,
                    "dbp": 6, "mbp": 7, "resp_rate": 11, "temperature": 12,
                    "spo2": 13},
    'CBC':{"id": 1, "charttime": 3, "hematocrit": 5,"hemoglobin": 6, "platelet": 7, "wbc": 8},
    'Vasoactive':{"id": 1, "starttime": 3, "dopamine": 5, "epinephrine": 6,
                "norepinephrine": 7, "phenylephrine": 8, "vasopressin":9,
                "dobutamine": 10, "milrinone": 11},
    'ABG':{"id": 1, "charttime": 3, "po2": 5, "pco2": 6, "pao2fio2ratio": 8,
            "ph": 9, "baseexcess": 10, "lactate": 11}
    

}


inflation_map = {
    'id': int,'age': float,'sex':sex_to_int,'deathtime': str,'hospital': str,'charttime': timestamp_to_ruby_time_str,
    'starttime': timestamp_to_ruby_time_str,'weight': float,'height': float,'step': str,'action': str,'time_CRRT': float,
    'time_IRRT': float,'gcs': float,'sofa': float,'inr': float,'pt': float,'ptt': float,'alt': float,
    'ast': float,'bilirubin': float,'respiratory_rate_set': float,'respiratory_rate_total': float,
    'respiratory_rate_spontaneous': float,'minute_volume': float,'tidal_volume_set': float,
    'tidal_volume_spontaneous': float,'plateau_pressure': float,'peep': float,'fio2': float,
    'ventilation_status': str,'uo_12': float,'uo_24': float,'albumin': float,'bicarbonate': float,
    'bun': float,'calcium': float,'chloride': float,'creatinine': float,'glucose': float,
    'sodium': float,'potassium': float,'magnesium': float,'heart_rate': float,'sbp': float,
    'dbp': float,'chartttime':timestamp_to_ruby_time_str,'mbp':float,'resp_rate':float,'temperature': float,
    'spo2':float, 'hematocrit': float,'hemoglobin': float,'platelet': float,'wbc': float,
    'dopamine': float,'epinephrine': float,'norepinephrine': float,'phenylephrine': float,
    'vasopressin': float,'dobutamine': float,'milrinone': float,'po2': float,'pco2': float,
    'pao2fio2ratio': float,'ph': float,'baseexcess': float,'lactate': float,
}

def load_excel(table, class_name, field_map, skip_header=True):
    list_obj = []
    cls = globals()[class_name]

    # 如果有表头，跳过第一行；否则从第 0 行开始
    start_idx = 1 if skip_header else 0

    for i in range(start_idx, table.shape[0]):
        row = table.iloc[i]  # 取第 i 行为 Series
        obj = cls()
        for attr, col_idx in field_map.items():
            val = row.iloc[col_idx]  # 根据列索引取值
            try:
                val = inflation_map[attr](val)
            except (ValueError, TypeError):
                if(val == None):
                    print(f'第{i+1}行，第{col_idx+1}列：值 {val}({attr})是None')
                else:
                    print(f"转换前，属性 {attr} 的值{val}类型为 {type(val)}")
                    print(f"[警告{class_name}] 第{i+1}行，第{col_idx+1}列：值 '{val}({attr})' 无法转换为 {inflation_map[attr].__name__}，已跳过或设置为 None")
                val = None  # 或者你可以选择 `continue`、设置为默认值等
            setattr(obj, attr, val)
        list_obj.append(obj)

    return list_obj