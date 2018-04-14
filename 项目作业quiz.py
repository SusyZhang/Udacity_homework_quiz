# -*- coding: utf-8 -*- 

supereasy_quiz = '入门'
easy_quiz = '简单'
medium_quiz = '中等'
hard_quiz = '困难'

questions = [supereasy_quiz, easy_quiz, medium_quiz, hard_quiz]

quiz = {supereasy_quiz:[('大海的颜色是__？','蓝色','无'),
                       ('今天的前一天是__？','昨天','无'),
                       ('今天的后一天是__？','明天','无'),
                       ('爸爸的妈妈我们叫__？','奶奶','无')],
        easy_quiz: [("中国的首都是__？",'北京','毛主席住在哪？'),
                    ('世界最高峰是__？','珠穆朗玛峰','属于喜马拉雅山脉'),
                    ('四川的省会是__？','成都','去哪里吃火锅！'),
                    ('江苏的省会是__?','南京','蒋委员长')],
        medium_quiz:[('阿根廷的首都是__？','布宜诺斯艾利斯','布宜*****'),
                     ('第一部诗歌总集是__？','诗经','*经'),
                     ('第一部纪传体通史是__？','史记','*记'),
                     ('第一部神话集是__？','山海经','山**')],
        hard_quiz:[('最大的海是__？','珊瑚海','珊**'),
                   ('钓鱼岛从__时就明确为我国的领土? ','明朝','和朱元璋有关的朝代～'),
                   ('三不朽是__？','立功立德立言','立功****'),
                   ('三教是__？','儒释道','儒**')]}

result = {'Correct': 0., "Incorrect":0.}

def get_quiz_nivel():
    while True:
        try:
            quiz_number = int(raw_input('{}～ 我们来玩一个答题游戏吧，告诉我你想玩什么难度的呢？\n1、{}\n2、{}\n3、{}\n4、{}\n你的选择是：'.format(name,supereasy_quiz,
                                                                                                    easy_quiz,
                                                                                                    medium_quiz,
                                                                                                    hard_quiz)))
        except ValueError:
            print '{}酱，你需要输入一个数字哦～\n'.format(name)
        else:
            if 0 >= quiz_number or quiz_number > len(quiz):
                print '{}酱～，请输入数字1，2，3，4！不要有空格～\n'.format(name)
            else:
                return quiz_number

name = raw_input('你好呀，请问你叫什么名字？')
choice = get_quiz_nivel()
quiz_nivel = questions[choice - 1]
print "\n你选择了{}!\n".format(quiz_nivel)

global limited_times
def limited_times():
    while True:
        try:
            limited_times = int(raw_input('告诉我每一题需要几次机会呀？'.format(name)))
        except ValueError:
            print '{}酱，你需要输入一个数字哦～\n'.format(name)
        else:
            return limited_times
limited_times = limited_times()
print '你有{}次机会!\n'.format(limited_times)

def get_answer(question,correct_answer,index,hint):
    attempted_times = 0
    while True:
        print "Q:{}".format(question)
        answer = raw_input('请回答～（请不要加空格( ´▽｀)！）')
        if answer == correct_answer:
            result["Correct"] += 1
            if index < len(quiz_questions):
                return "回答正确！小{}你真棒!继续下一题的挑战吧！".format(name)
            elif index == len(quiz_questions):
                return '回答正确！小{}你太厉害了，本级别你已经回答完毕(#^.^#)！快去挑战更难的级别吧！'.format(name)   
        else:
            if attempted_times == (int(limited_times)-1):
                result['Incorrect'] += 1
                return '真可惜，此题的回答次数已用尽:( '
            else:
                left_times = (int(limited_times)-1) - attempted_times
                print "不正确，你还有{}次机会，请再试试！( ̀⌄ ́)（提示：{}）".format(left_times,single_hint)
                attempted_times += 1

            
quiz_questions = quiz[quiz_nivel]
index = 0
for q in (quiz_questions):
    index += 1
    single_question = q[0]
    single_correct_answer = q[1]
    single_hint = q[2]
    answer_result = get_answer(single_question,single_correct_answer,index,single_hint)
    complet_correct_answer = single_question.replace('__？',single_correct_answer)
    print '\n{} \n（^ - ^!{}！）\n'.format(answer_result,complet_correct_answer)

totally_answered = len(quiz_questions)
user_correct = result['Correct']
correct_rate = user_correct/totally_answered
correct_rate_percent = '%.2f%%' % (correct_rate * 100)
print '{}，你共回答了{}题, 答对了{}题，正确率为：{}!'.format(name,totally_answered,user_correct,correct_rate_percent)

#参考 https://codereview.stackexchange.com/questions/22822/simple-quiz-program


