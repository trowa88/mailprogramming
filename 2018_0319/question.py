"""
간격(interval)로 이루어진 배열이 주어지면, 겹치는 간격 원소들을 합친 새로운 배열을 만드시오. 간격은 시작과 끝으로 이루어져 있으며 시작은 끝보다 작거나 같습니다.


예제)
Input: {{2,4}, {1,5}, {7,9}}

Output: {{1,5}, {7,9}}


Input: {{3,6}, {1,3}, {2,4}}

Output: {{1,6}}
"""


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return '{' + str(self.start) + ', ' + str(self.end) + '}'


def merge(interval_list_):
    result = []
    for interval in interval_list_:
        if not result:
            result.append(interval)
            continue
        # [1, 5] [2, 4]
        if result[0].end >= interval.start:
            result[0].start = result[0].start if result[0].start < interval.start else interval.start
            result[0].end = result[0].end if result[0].end > interval.end else interval.end
        else:
            result.append(interval)
    return result


interval_list = [
    Interval(2, 4),
    Interval(1, 5),
    Interval(7, 9)
]

print(merge(sorted(interval_list, key=lambda x: x.start)))

interval_list.clear()
interval_list.append(Interval(3, 6))
interval_list.append(Interval(1, 3))
interval_list.append(Interval(2, 4))

print(merge(sorted(interval_list, key=lambda x: x.start)))
