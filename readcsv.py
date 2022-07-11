import pandas as pd
import requests,json,numpy

#link https://nguyenvanhieu.vn/thu-vien-pandas-python/
def get_json_150():
    URL =  "https://api-csn-sun.gameland.vip/api/v1/round/ended?limit=150&page=1&tableId=103"
    return json.loads(requests.get(URL).text)["content"]



def read_dataframe():
	df = pd.read_csv('data.csv',index_col = 0)
	return df

def create_dataframe():
	js = get_json_150()
	df = pd.DataFrame(js)
	df.drop('table', axis=1, inplace=True)
	df.drop('startAt', axis=1, inplace=True)
	df.drop('endAt', axis=1, inplace=True)
	df.drop('startAtDate', axis=1, inplace=True)
	df.drop('endAtDate', axis=1, inplace=True)
	df.drop('status', axis=1, inplace=True)
	df.drop('createdDate', axis=1, inplace=True)
	df.drop('updatedDate', axis=1, inplace=True)
	df.drop('timeBet', axis=1, inplace=True)
	df.drop('currentTime', axis=1, inplace=True)
	df.drop('timeBetCountdown', axis=1, inplace=True)
	df.sort_values('id', ascending=True,inplace=True)
	df.dropna(how="any",inplace=True)
	# df.to_csv('data.csv')
	return df

def add_dataframe():
	olddf = read_dataframe()
	maxid = max(olddf['id'])
	text = "id>"+str(maxid)
	newdf = create_dataframe()
	newdf.query(text,inplace=True)
	zipdf = pd.concat([olddf,newdf])
	zipdf.to_csv('data.csv')


	