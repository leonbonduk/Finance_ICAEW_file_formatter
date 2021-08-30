import glob

#list all files in directory
file_list = glob.glob('C:/Users/user/Documents/Python Projects/ICAEW data formatter/data/*')

for fl in file_list:
    f = open(fl, 'r') #open read only
    data = f.read().split('\n') #data entered into list at each new line break
    data.pop() # remove last blank line

    #outt put file created with string from filanme path from the last /
    out_file_name = 'C:/Users/user/Documents/Python Projects/ICAEW data formatter/data/*' + fl.split('/')[-1]
    fo = open(out_file_name, 'w')
    headers = data[0]
    fo.write(headers + '\n')
    # capture data from 2nd row since first are headers
    data = data[1:]
    for d in data:
        date, value, currency = d.split(',')

        # to format data idf mixture of split by hyoens and slashes
        date_split = date.split('-')
        if len(date_split) ==1:
            #date format is yyyy/mm/dd
            year, month, day = date.split('/')
        elif len(date_split[0]) == 2:
            # date format is mm-dd-yyy
            month, day, year = date_split
        else:
            #date format is yyyy-mm-dd
            year, month, day = date.split

        new_date = year + '-' + month + '-' + day
        if currency in ['USD', '$']:
            currency = 'USD'
        if currency in ['GBP', '£']:
            currency = 'GBP'

        out_str = new_date + ',' + value + ',' + currency + '\n'
        fo.write(out_str)

    f.close()
    fo.close()

