#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd

from sklearn.preprocessing import StandardScaler

class PreprocessData:

    def readData(self,file):
        df = pd.read_csv(file)
        return df

    def writeData(self,df,file,):
        df.to_csv(file,index=False)

    def dropColumns(self,df,columns):
        df = df.drop(columns,axis=1)
        return df

    def dealCVVVPt(self,df,columns):
        scaler = StandardScaler()
        df[columns] = scaler.fit_transform(df[columns])
        return df

    def dealUi_ver(self,df):
        #df['ui_ver'].replace('^-$', '0', regex=True, inplace=True)
        dummies_ui_ver = pd.get_dummies(df['ui_ver'], prefix='ui_ver')
        df = df.drop(['ui_ver'], axis=1)
        df = pd.concat([df, dummies_ui_ver], axis=1)
        return df

    def dealMain_desk(self,df):
        dummies_main_desk = pd.get_dummies(df['main_desk'], prefix='main_desk')
        df = df.drop(['main_desk'], axis=1)
        df = pd.concat([df, dummies_main_desk], axis=1)
        return df

    def dealDistrict_name(self,df):
        dummies_district_name = pd.get_dummies(df['district_name'], prefix='district_name')
        df = df.drop(['district_name'], axis=1)
        df = pd.concat([df, dummies_district_name], axis=1)
        return df

    def dealPlayDays(self,df):
        df.loc[df['play_days'] <= 4, 'play_days'] = 0
        df.loc[(df['play_days'] > 4) & (df['play_days'] <= 15), 'play_days'] = 1
        df.loc[(df['play_days'] > 15) & (df['play_days'] <= 27), 'play_days'] = 2
        df.loc[df['play_days'] > 27, 'play_days'] = 4

        dummies_play_days = pd.get_dummies(df['play_days'], prefix='play_days')
        df = df.drop(['play_days'], axis=1)
        df = pd.concat([df, dummies_play_days], axis=1)
        return df

    def dealCV(self,df):
        df.loc[df['cv'] <= df['cv'].quantile(0.25), 'cv'] = 0
        df.loc[(df['cv'] > df['cv'].quantile(0.25)) & (df['cv'] <= df['cv'].quantile(0.5)), 'cv'] = 1
        df.loc[(df['cv'] > df['cv'].quantile(0.5)) & (df['cv'] <= df['cv'].quantile(0.75)), 'cv'] = 2
        df.loc[df['cv'] > df['cv'].quantile(0.75), 'cv'] = 4

        dummies_play_days = pd.get_dummies(df['cv'], prefix='cv')
        df = df.drop(['cv'], axis=1)
        df = pd.concat([df, dummies_play_days], axis=1)
        return df

    def dealPT(self,df):
        df.loc[df['pt'] <= df['pt'].quantile(0.25), 'pt'] = 0
        df.loc[(df['pt'] > df['pt'].quantile(0.25)) & (df['pt'] <= df['pt'].quantile(0.5)), 'pt'] = 1
        df.loc[(df['pt'] > df['pt'].quantile(0.5)) & (df['pt'] <= df['pt'].quantile(0.75)), 'pt'] = 2
        df.loc[df['pt'] > df['pt'].quantile(0.75), 'pt'] = 4

        dummies_play_days = pd.get_dummies(df['pt'], prefix='pt')
        df = df.drop(['pt'], axis=1)
        df = pd.concat([df, dummies_play_days], axis=1)
        return df

    def dealStart_times(self,df):
        df.loc[df['start_times'] <= df['start_times'].quantile(0.25), 'start_times'] = 0
        df.loc[(df['start_times'] > df['start_times'].quantile(0.25)) & (df['start_times'] <= df['start_times'].quantile(0.5)), 'start_times'] = 1
        df.loc[(df['start_times'] > df['start_times'].quantile(0.5)) & (df['start_times'] <= df['start_times'].quantile(0.75)), 'start_times'] = 2
        df.loc[df['start_times'] > df['start_times'].quantile(0.75), 'start_times'] = 4

        dummies_play_days = pd.get_dummies(df['start_times'], prefix='start_times')
        df = df.drop(['start_times'], axis=1)
        df = pd.concat([df, dummies_play_days], axis=1)
        return df

    def dealClose_times(self,df):
        df.loc[df['close_times'] <= df['close_times'].quantile(0.25), 'close_times'] = 0
        df.loc[(df['close_times'] > df['close_times'].quantile(0.25)) & (df['close_times'] <= df['close_times'].quantile(0.5)), 'close_times'] = 1
        df.loc[(df['close_times'] > df['close_times'].quantile(0.5)) & (df['close_times'] <= df['close_times'].quantile(0.75)), 'close_times'] = 2
        df.loc[df['close_times'] > df['close_times'].quantile(0.75), 'close_times'] = 4

        dummies_play_days = pd.get_dummies(df['close_times'], prefix='close_times')
        df = df.drop(['close_times'], axis=1)
        df = pd.concat([df, dummies_play_days], axis=1)
        return df

    def dealDuration(self, df):
        df.loc[df['duration'] <= df['duration'].quantile(0.22), 'duration'] = 0
        df.loc[(df['duration'] > df['duration'].quantile(0.2)) & (df['duration'] <= df['duration'].quantile(0.4)), 'duration'] = 1
        df.loc[(df['duration'] > df['duration'].quantile(0.4)) & (df['duration'] <= df['duration'].quantile(0.6)), 'duration'] = 2

        df.loc[(df['duration'] > df['duration'].quantile(0.6)) & (df['duration'] <= df['duration'].quantile(0.8)), 'duration'] = 3

        df.loc[df['duration'] > df['duration'].quantile(0.8), 'duration'] = 4

        dummies_play_days = pd.get_dummies(df['duration'], prefix='duration')
        df = df.drop(['duration'], axis=1)
        df = pd.concat([df, dummies_play_days], axis=1)
        return df

    def dealContinuousToDiscrete(self,df,columns):
        df.loc[df[columns] <= df[columns].quantile(0.25), columns] = 0
        df.loc[(df[columns] > df[columns].quantile(0.25)) & (df[columns] <= df[columns].quantile(0.5)), columns] = 1
        df.loc[(df[columns] > df[columns].quantile(0.5)) & (df[columns] <= df[columns].quantile(0.75)), columns] = 2
        df.loc[df[columns] > df[columns].quantile(0.75), columns] = 3

        dummies_play_days = pd.get_dummies(df[columns], prefix=columns)
        df = df.drop([columns], axis=1)
        df = pd.concat([df, dummies_play_days], axis=1)
        return df

class SampleData:
    pass
