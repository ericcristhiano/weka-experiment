import pandas as pd
import numpy as np

df = pd.read_csv('src/imoveis.csv', delimiter=',')

df = df.drop('id', 1)
df = df.drop('bathroom', 1)

areas_bins = [0, 50, 100, 150, 200, 300, 400, 500, 600, 700, 800, 900, 1000, np.inf]
areas_labels = ['0-50', '51-100', '101-150', '151-200', '201-300', '301-400', '401-500', '501-600', '601-700', '701-800', '801-900', '901-1000', '1001+']

floor_bins = [0, 5, 10, 15, 20, 25, 30, 35, np.inf]
floor_labels = ['0-5', '6-10', '11-15', '16-20', '21-25', '26-30', '31-35', '36+']

total_bins = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 15000, 20000, np.inf]
total_labels = [
    '0-1000', '1001-2000', '2001-3000', '3001-4000', '4001-5000', '5001-6000', '6001-7000',
    '7001-8000', '8001-9000', '9001-10000', '10001-15000', '15001-20000', '20001+']

hoa_bins = [0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, np.inf]
hoa_labels = [
    '0-500', '501-1000', '1001-1500', '1501-2000', '2001-2500', '2501-3000', '3001-3500',
    '3501-4000', '4001-4500', '4501-5000', '5001+']

rent_amount_bins = [0, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 6000, 7000, 8000, 9000, 10000, 15000, np.inf]
rent_amount_labels = [
    '0-1000', '1001-1500', '1501-2000', '2001-2500', '2501-3000', '3001-3500',
    '3501-4000', '4001-4500', '4501-5000', '5001-6000', '6001-7000', '7001-8000', '8001-9000',
    '9001-10000', '10001-15000', '15001+']

property_tax_bins = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800, 900, 1000, 1500, 2000, 2500, 3000, 3500, 4000, np.inf]
property_tax_labels = [
    '0-50', '51-100', '101-150', '151-200', '201-250', '251-300', '301-350', '351-400', '401-450',
    '451-500', '501-600', '601-700', '701-800', '801-900', '901-1000', '1001-1500', '1501-2000', '2001-2500',
    '2501-3000', '3001-3500', '3501-4000', '4001+']

fire_insurance_bins = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, np.inf]
fire_insurance_labels = [
    '0-20', '21-40', '41-60', '61-80', '81-100', '101-120', '121-140', '141-160', '161-180',
    '181-200', '201-220', '221-240', '241+']

df['area'] = pd.cut(df['area'],
                      bins=areas_bins,
                      labels=areas_labels,
                    include_lowest=True)

df['floor'] = pd.cut(df['floor'],
                      bins=floor_bins,
                      labels=floor_labels,
                     include_lowest=True)

df['hoa'] = pd.cut(df['hoa'],
                      bins=hoa_bins,
                      labels=hoa_labels,
                     include_lowest=True)

df['rent amount'] = pd.cut(df['rent amount'],
                      bins=rent_amount_bins,
                      labels=rent_amount_labels,
                     include_lowest=True)

df['property tax'] = pd.cut(df['property tax'],
                      bins=property_tax_bins,
                      labels=property_tax_labels,
                     include_lowest=True)

df['fire insurance'] = pd.cut(df['fire insurance'],
                      bins=fire_insurance_bins,
                      labels=fire_insurance_labels,
                     include_lowest=True)

df['total'] = pd.cut(df['total'],
                      bins=total_bins,
                      labels=total_labels,
                     include_lowest=True)

with open('src/imoveis.arff', 'w') as f:
    # name
    f.write('@relation imoveis\n\n')
    # attributes
    f.write('@attribute cidade{0,1}\n')
    f.write('@attribute area{}\n'.format('{' + ','.join(areas_labels) + '}'))
    f.write('@attribute quartos{}\n'.format('{' + ','.join(['1', '2', '3', '4', '5', '6', '7', '8', '10']) + '}'))
    f.write('@attribute vagas{}\n'.format('{' + ','.join(['0', '1', '2', '3', '4', '5', '6', '7', '8', '12']) + '}'))
    f.write('@attribute andar{}\n'.format('{' + ','.join(floor_labels) + '}'))
    f.write('@attribute animal{0,1}\n')
    f.write('@attribute mobiliado{0,1}\n')
    f.write('@attribute condominio{}\n'.format('{' + ','.join(hoa_labels) + '}'))
    f.write('@attribute aluguel{}\n'.format('{' + ','.join(rent_amount_labels) + '}'))
    f.write('@attribute iptu{}\n'.format('{' + ','.join(property_tax_labels) + '}'))
    f.write('@attribute seguro_incendio{}\n'.format('{' + ','.join(fire_insurance_labels) + '}'))
    f.write('@attribute total{}\n'.format('{' + ','.join(total_labels) + '}\n'))
    # data
    f.write('@data\n')

    for index, row in df.iterrows():
        for column_index, column in enumerate(row.values):
            f.write('{}\t'.format(column))
        f.write('\n')
