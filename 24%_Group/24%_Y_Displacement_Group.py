# 24% Y displacement - cotton, acrylic

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("start:")

print("reading files...")
elastic_data = pd.read_excel(r'Abdominal Compression Data.xlsx', sheet_name="24%-total")


elastic1_x = list(elastic_data['Y_NominalStrain_%_elastic1'])
elastic1_y = list(elastic_data['Y_Force_mN_elastic1'])

elastic2_x = list(elastic_data['Y_NominalStrain_%_elastic2'])
elastic2_y = list(elastic_data['Y_Force_mN_elastic2'])

elastic3_x = list(elastic_data['Y_NominalStrain_%_elastic3'])
elastic3_y = list(elastic_data['Y_Force_mN_elastic3'])



print("plotting lines...")
#acrylic_data.plot.line('X_NominalStrain_%_acrylic1', 'X_Force_mN_acrylic1')
plt.plot(elastic1_x, elastic1_y, label='elastic 1')
plt.plot(elastic2_x, elastic2_y, label='elastic 2')
plt.plot(elastic3_x, elastic3_y, label='elastic 3')


plt.legend()
plt.xlabel('Y Nominal Strain %')
plt.ylabel('Y Force (mN)')
plt.title('24% Y Displacement Group (elastic)')


plt.show()

print("end.")

