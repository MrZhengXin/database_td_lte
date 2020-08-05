'''
f = open('sql.temp', 'w')
for i in range(100):
    if i % 10 == 0:
        print(file=f)
    print('avg([第%d个prb上检测到的干扰噪声的平均值_field]) as [第%d个prb上检测到的干扰噪声的平均值_field]' % (i, i), end=', ', file=f)
'''
for i in range(100):
    print('ALTER TABLE [dbo].[tbPRBnew] ALTER COLUMN [第%d个PRB上检测到的干扰噪声的平均值_field] float(255) NULL\nGO\n' % (i))