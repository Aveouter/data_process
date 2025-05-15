class base():
    def __init__(self):
        self.id = ''
        self.age = ''
        self.sex = ''
        self.deathtime = ''
        self.hospital = ''

class BMI():
    def __init__(self):
        self.id = ''
        self.charttime = ''
        self.starttime = ''
        self.weight = ''
        self.height = ''

class CRRT():
    def __init__(self):
        self.id = ''
        self.starttime = ''
        self.step = ''
        self.action = ''
        self.time_CRRT= ''
        self.time_IRRT = ''

class gcs():
    def __init__(self):
        self.id = ''
        self.starttime = ''
        self.gcs = ''

class sofa():
    def __init__(self):
        self.id = ''
        self.starttime = ''
        self.sofa = ''

class coagulation():
    def __init__(self):
        self.id = ''
        self.charttime = ''
        self.inr = ''
        self.pt = ''
        self.ptt = ''

class LFTs():
    def __init__(self):
        self.id = ''
        self.charttime = ''
        self.alt = ''
        self.ast = ''
        self.bilirubin = ''

class Ventilator():
    def __init__(self):
        self.id = ''
        self.charttime = ''
        self.respiratory_rate_set = ''
        self.respiratory_rate_total = ''
        self.respiratory_rate_spontaneous = ''
        self.minute_volume = ''
        self.tidal_volume_set = ''
        self.tidal_volume_spontaneous = ''
        self.plateau_pressure = ''
        self.peep = ''
        self.fio2 = ''

class MV():
    def __init__(self):
        self.id = ''
        self.starttime = ''
        self.ventilation_status = ''

class UO():
    def __init__(self):
        self.id = ''
        self.chartttime = ''
        self.uo_12 = ''
        self.uo_24 = ''

class Biochemistry():
    def __init__(self):
        self.id = ''
        self.charttime = ''
        self.albumin = ''
        self.bicarbonate = ''
        self.bun = ''
        self.calcium = ''
        self.chloride = ''
        self.creatinine = ''
        self.glucose = ''
        self.sodium = ''
        self.potassium = ''
        self.magnesium = ''

class Vitalsigns():
    def __init__(self):
        self.id = ''
        self.charttime = ''
        self.heart_rate = ''
        self.sbp = ''
        self.dbp = ''
        self.mbp = ''
        self.resp_rate = ''
        self.temperature = ''
        self.spo2 = ''

class CBC():
    def __init__(self):
        self.id = ''
        self.charttime = ''
        self.hematocrit = ''
        self.hemoglobin = ''
        self.platelet = ''
        self.wbc = ''

class Vasoactive():
    def __init__(self):
        self.id = ''
        self.starttime = ''
        self.dopamine = ''
        self.epinephrine = ''
        self.norepinephrine = ''
        self.phenylephrine = ''
        self.vasopressin = ''
        self.dobutamine = ''
        self.milrinone = ''

class ABG():
    def __init__(self):
        self.id = ''
        self.charttime = ''
        self.po2 = ''
        self.pco2 = ''
        self.pao2fio2ratio = ''
        self.ph = ''
        self.baseexcess = ''
        self.lactate = ''

class sick():
    def __init__(self):
        self.id = ''
        self.step = ''
        self.starttime = ''

        self.age = ''
        self.sex = ''
        self.deathtime = ''
        self.hospital = ''

        # From BMI
        self.weight = ''
        self.height = ''

        # From CRRT
        self.action = ''
        self.time_CRRT = ''
        self.time_IRRT = ''

        # From gcs
        self.gcs = ''

        # From sofa
        self.sofa = ''

        # From coagulation
        self.inr = ''
        self.pt = ''
        self.ptt = ''

        # From LFTs
        self.alt = ''
        self.ast = ''
        self.bilirubin = ''

        # From Ventilator
        self.respiratory_rate_set = ''
        self.respiratory_rate_total = ''
        self.respiratory_rate_spontaneous = ''
        self.minute_volume = ''
        self.tidal_volume_set = ''
        self.tidal_volume_spontaneous = ''
        self.plateau_pressure = ''
        self.peep = ''
        self.fio2 = ''

        # From MV
        self.ventilation_status = ''

        # From UO
        self.uo_12 = ''
        self.uo_24 = ''

        # From Biochemistry()
        self.albumin = ''
        self.bicarbonate = ''
        self.bun = ''
        self.calcium = ''
        self.chloride = ''
        self.creatinine = ''
        self.glucose = ''
        self.sodium = ''
        self.potassium = ''
        self.magnesium = ''

        # From Vitalsigns()
        self.heart_rate = ''
        self.sbp = ''
        self.dbp = ''
        self.mbp = ''
        self.resp_rate = ''
        self.temperature = ''
        self.spo2 = ''

        # From CBC()
        self.hematocrit = ''
        self.hemoglobin = ''
        self.platelet = ''
        self.wbc = ''

        # From Vasoative()
        self.dopamine = ''
        self.epinephrine = ''
        self.norepinephrine = ''
        self.phenylephrine = ''
        self.vasopressin = ''
        self.dobutamine = ''
        self.milrinone = ''

        # From ABG()
        self.po2 = ''
        self.pco2 = ''
        self.pao2fio2ratio = ''
        self.ph = ''
        self.baseexcess = ''
        self.lactate = ''
