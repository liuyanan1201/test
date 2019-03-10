import xlrd

def get_sheet(file,name):
    excel = xlrd.open_workbook(file)
    sheet = excel.sheet_by_name(name)
    return sheet

def get_case(sheet,case_name):
    for i in range(1,sheet.nrows):
        if sheet.cell(i,0).value == case_name:
            return sheet.row_values(i)
    return None


if __name__ == '__main__':
    sh = get_sheet("../data/data.xls","登录")
    print(sh)

    case_data = get_case(sh,"test_user_login_normal")
    print(case_data)