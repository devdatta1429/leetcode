class Solution(object):
    def toHex(self, num):
        if num == 0:
             return "0"

        if num < 0 :
            num = num & 0xffffffff

        result = ""

        while num > 0:
            remain = num%16
            quo = num//16

            if remain<10:
                result = str(remain) + result
            else:
                result = chr(87+remain) + result

            num=quo

        return result