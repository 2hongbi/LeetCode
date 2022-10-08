import string


class Solution(object):
    def check_ip_v4(self, ipv4):
        ipnums = ipv4.split('.')
        
        for num in ipnums:
            if len(num) == 0 or len(num) > 3:
                return 'Neither'
            
            if (len(num) != 1 and num[0] == '0') or not num.isdigit() or int(num) > 255:
                return 'Neither'
        return 'IPv4'
    
    def check_ip_v6(self, ipv6):
        ipnums = ipv6.split(':')
        for num in ipnums:
            if len(num) == 0 or len(num) > 4 or not all(c in string.hexdigits for c in num):
                return 'Neither'
        return 'IPv6'
    
    
    def validIPAddress(self, queryIP):
        """
        :type queryIP: str
        :rtype: str
        """
        if queryIP.count('.') == 3:
            return self.check_ip_v4(queryIP)
        elif queryIP.count(':') == 7:
            return self.check_ip_v6(queryIP)
        
        return 'Neither'
        