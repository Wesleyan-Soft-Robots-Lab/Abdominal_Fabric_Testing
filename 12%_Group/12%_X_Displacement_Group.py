# 12% X displacement - cotton, acrylic

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("start:")

print("reading files...")
displacement_data = pd.read_excel(r'Abdominal Compression Data.xlsx', sheet_name="12%-total")


acrylic1_x = list(displacement_data['X_NominalStrain_%_acrylic1'])
acrylic1_y = list(displacement_data['X_Force_mN_acrylic1'])

acrylic2_x = list(displacement_data['X_NominalStrain_%_acrylic2'])
acrylic2_y = list(displacement_data['X_Force_mN_acrylic2'])

acrylic3_x = list(displacement_data['X_NominalStrain_%_acrylic3'])
acrylic3_y = list(displacement_data['X_Force_mN_acrylic3'])

cotton1_x = list(displacement_data['X_NominalStrain_%_cotton1'])
cotton1_y = list(displacement_data['X_Force_mN_cotton1'])

cotton2_x = list(displacement_data['X_NominalStrain_%_cotton2'])
cotton2_y = list(displacement_data['X_Force_mN_cotton2'])

cotton3_x = list(displacement_data['X_NominalStrain_%_cotton3'])
cotton3_y = list(displacement_data['X_Force_mN_cotton3'])


print("plotting lines...")

plt.plot(acrylic1_x, acrylic1_y, label='acrylic 1', color='skyblue')
plt.plot(acrylic2_x, acrylic2_y, label='acrylic 2', color='royalblue')
plt.plot(acrylic3_x, acrylic3_y, label='acrylic 3', color='navy')

plt.plot(cotton1_x, cotton1_y, label='cotton 1', color='indianred')
plt.plot(cotton2_x, cotton2_y, label='cotton 2', color='firebrick')
plt.plot(cotton3_x, cotton3_y, label='cotton 3', color='maroon')


plt.legend()
plt.xlabel('X Nominal Strain %')
plt.ylabel('X Force (mN)')
plt.title('12% X Displacement Group (cotton, acrylic)')


plt.show()

print("end.")

