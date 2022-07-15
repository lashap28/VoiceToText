import pandas as pd
from voiceService import db
from voiceService import Word

if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    a = pd.read_excel('words.xlsx')
    for i in range(a.shape[0]):
        db.session.add(Word(id=i, word=a.iloc[i,1]))
    db.session.commit()