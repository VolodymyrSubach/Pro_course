def get_score_list():
    with open('src_14.txt', mode='r') as file:
        average_score_list = []
        for i in file:
            average_score = []
            pupil_list = i.split()
            for j in pupil_list:
                if j.isdigit():
                    average_score.append(int(j))

            average_score_list.append(
                (pupil_list[1] + ' ' + i[0] + '.', round(sum(average_score) / len(average_score), 2)))

        return average_score_list


def output_result(score_list):
    with open('average_score_log.txt', 'w') as file:
        average_group_score = 0
        counter = 0
        for i in score_list:
            average_group_score += i[1]
            counter += 1
            file.write(f'{i[0]:<21} {i[1]:<5}\n')

            if i[1] < 5:
                print(f'{i[0]:<21} {i[1]:<5}')

        print(f'\nСредний балл класса: {round(average_group_score / counter, 2):>5}')


output_result(get_score_list())
