# 6% X displacement - cottonfishing, acrylicfishing, elasticfishing

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("start:")

print("reading files...")
displacement_data = pd.read_excel(r'Abdominal Compression Data.xlsx', sheet_name="6%-total")


cottonfishing1_x = list(displacement_data['X_NominalStrain_%_cottonfishing1'])
cottonfishing1_y = list(displacement_data['X_Force_mN_cottonfishing1'])

cottonfishing2_x = list(displacement_data['X_NominalStrain_%_cottonfishing2'])
cottonfishing2_y = list(displacement_data['X_Force_mN_cottonfishing2'])

cottonfishing3_x = list(displacement_data['X_NominalStrain_%_cottonfishing3'])
cottonfishing3_y = list(displacement_data['X_Force_mN_cottonfishing3'])


acrylicfishing1_x = list(displacement_data['X_NominalStrain_%_acrylicfishing1'])
acrylicfishing1_y = list(displacement_data['X_Force_mN_acrylicfishing1'])

acrylicfishing2_x = list(displacement_data['X_NominalStrain_%_acrylicfishing2'])
acrylicfishing2_y = list(displacement_data['X_Force_mN_acrylicfishing2'])

acrylicfishing3_x = list(displacement_data['X_NominalStrain_%_acrylicfishing3'])
acrylicfishing3_y = list(displacement_data['X_Force_mN_acrylicfishing3'])


elasticfishing1_x = list(displacement_data['X_NominalStrain_%_elasticfishing1'])
elasticfishing1_y = list(displacement_data['X_Force_mN_elasticfishing1'])

elasticfishing2_x = list(displacement_data['X_NominalStrain_%_elasticfishing2'])
elasticfishing2_y = list(displacement_data['X_Force_mN_elasticfishing2'])

elasticfishing3_x = list(displacement_data['X_NominalStrain_%_elasticfishing3'])
elasticfishing3_y = list(displacement_data['X_Force_mN_elasticfishing3'])



print("plotting lines...")

plt.plot(cottonfishing1_x, cottonfishing1_y, label='cottonfishing 1', color='indianred')
plt.plot(cottonfishing2_x, cottonfishing2_y, label='cottonfishing 2', color='firebrick')
plt.plot(cottonfishing3_x, cottonfishing3_y, label='cottonfishing 3', color='maroon')

plt.plot(acrylicfishing1_x, acrylicfishing1_y, label='acrylicfishing 1', color='skyblue')
plt.plot(acrylicfishing2_x, acrylicfishing2_y, label='acrylicfishing 2', color='royalblue')
plt.plot(acrylicfishing3_x, acrylicfishing3_y, label='acrylicfishing 3', color='navy')

plt.plot(elasticfishing1_x, elasticfishing1_y, label='elasticfishing 1', color='violet')
plt.plot(elasticfishing2_x, elasticfishing2_y, label='elasticfishing 2', color='mediumorchid')
plt.plot(elasticfishing3_x, elasticfishing3_y, label='elasticfishing 3', color='purple')


plt.legend()
plt.xlabel('X Nominal Strain %')
plt.ylabel('X Force (mN)')
plt.title('6% X Displacement Group (cottonfishing, acrylicfishing, elasticfishing)')


plt.show()

print("end.")

