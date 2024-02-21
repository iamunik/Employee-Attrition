def cleaned(data):
    data['BusinessTravel'] = data['BusinessTravel'].map({'Travel_Rarely': 0,
                                                         'Travel_Frequently': 1,
                                                         'Non-Travel': 2}).astype('int64')
    data['Department'] = data['Department'].map({'Sales': 0,
                                                 'Research & Development': 1,
                                                 'Human Resources': 2}).astype('int64')

    data['EducationField'] = data['EducationField'].map({'Life Sciences': 0,
                                                         'Medical': 1,
                                                         'Marketing': 2,
                                                         'Technical Degree': 3,
                                                         'Human Resources': 4,
                                                         'Other': 5}).astype('int64')

    data['Gender'] = data['Gender'].map({'Male': 0,
                                         'Female': 1}).astype('int64')

    data['OverTime'] = data['OverTime'].map({'No': 0,
                                             'Yes': 1}).astype('int64')

    # data['Attrition'] = data['Attrition'].map({'No': 0,
    #                                            'Yes': 1}).astype('int64')

    data['MaritalStatus'] = data['MaritalStatus'].map({'Single': 0,
                                                       'Married': 1,
                                                       'Divorced': 2}).astype('int64')

    data['JobRole'] = data['JobRole'].map({'Sales Executive': 0,
                                           'Research Scientist': 1,
                                           'Laboratory Technician': 2,
                                           'Manufacturing Director': 3,
                                           'Healthcare Representative': 4,
                                           'Manager': 5,
                                           'Sales Representative': 6,
                                           'Research Director': 7,
                                           'Human Resources': 8}).astype('int64')

    return data
