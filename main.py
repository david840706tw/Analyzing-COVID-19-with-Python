from matplotlib.pyplot import axis
import pandas as pd
import matplotlib.pyplot as plt

confirmed = pd.read_csv('covid19_confirmed.csv')
deaths = pd.read_csv('covid19_deaths.csv')
recovered = pd.read_csv('covid19_recovered.csv')

confirmed = confirmed.drop(['Province/State', 'Lat', 'Long'], axis=1)
deaths = deaths.drop(['Province/State', 'Lat', 'Long'], axis=1)
recovered = recovered.drop(['Province/State', 'Lat', 'Long'], axis=1)

confirmed = confirmed.groupby(confirmed['Country/Region']).aggregate('sum')
deaths = deaths.groupby(deaths['Country/Region']).aggregate('sum')
recovered = recovered.groupby(recovered['Country/Region']).aggregate('sum')

confirmed = confirmed.T
deaths = deaths.T
recovered = recovered.T

# print(deaths)
# print(recovered)

new_cases = confirmed.copy()

for day in range(1, len(confirmed)):
    new_cases.iloc[day] = confirmed.iloc[day] - confirmed.iloc[day - 1]

# print(new_cases.tail(10))
# print(confirmed.tail(10))

growth_rate = confirmed.copy()

for day in range(1, len(confirmed)):
    growth_rate.iloc[day] = (new_cases.iloc[day] /
                             confirmed.iloc[day - 1]) * 100

# print(growth_rate.tail(10))

active_cases = confirmed.copy()

for day in range(0, len(confirmed)):
    active_cases.iloc[day] = confirmed.iloc[day] - \
        deaths.iloc[day] - recovered.iloc[day]

overall_growth_rate = confirmed.copy()

for day in range(1, len(confirmed)):
    overall_growth_rate.iloc[day] = (
        (active_cases.iloc[day] - active_cases.iloc[day - 1]) / active_cases.iloc[day - 1]) * 100

print(overall_growth_rate['Taiwan'].tail(10))

death_rate = confirmed.copy()

for day in range(0, len(confirmed)):
    death_rate.iloc[day] = (deaths.iloc[day] / confirmed.iloc[day]) * 100

hospitalization_rate_estimate = 0.05

hospitalization_needed = confirmed.copy()

for day in range(0, len(confirmed)):
    hospitalization_needed.iloc[day] = active_cases.iloc[day] * \
        hospitalization_rate_estimate

# Visualization

# countries = ['Italy', 'Austria', 'US', 'China',
#              'India', 'Taiwan', 'France', 'Spain']

# ax = plt.subplot()
# ax.set_facecolor('black')
# ax.figure.set_facecolor('#121212')
# ax.tick_params(axis='x', colors='white')
# ax.tick_params(axis='y', colors='white')
# ax.set_title('COVID_19 - Total Confirmed Cases By County', color='white')


# for country in countries:
#     confirmed[country][35:].plot(label=country)

# plt.legend(loc='upper left')
# plt.show()

# countries = ['Italy', 'Germany', 'US', 'China']

# for country in countries:
#     ax = plt.subplot()
#     ax.set_facecolor('black')
#     ax.figure.set_facecolor('#121212')
#     ax.tick_params(axis='x', colors='white')
#     ax.tick_params(axis='y', colors='white')
#     ax.set_title(
#         f'COVID_19 - Confirmed Cases Growth Rate {country}', color='white')
#     growth_rate[country].plot.bar()
#     plt.show()


# countries = ['Italy', 'Germany', 'US', 'China']

# ax = plt.subplot()
# ax.set_facecolor('black')
# ax.figure.set_facecolor('#121212')
# ax.tick_params(axis='x', colors='white')
# ax.tick_params(axis='y', colors='white')
# ax.set_title('COVID_19 - Total Deaths By County', color='white')


# for country in countries:
#     deaths[country].plot(label=country)

# plt.legend(loc='upper left')
# plt.show()

countries = ['Italy', 'Germany', 'US', 'China', 'Spain', 'France']

ax = plt.subplot()
ax.set_facecolor('black')
ax.figure.set_facecolor('#121212')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.set_title('COVID_19 - Total Deaths By County', color='white')


for country in countries:
    deaths[country].plot(label=country)

plt.legend(loc='upper left')
plt.show()
