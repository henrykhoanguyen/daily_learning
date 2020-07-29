class Solution:
    def validIPAddress(self, IP: str) -> str:
        if IP.count(".") == 3:
            def validateIPv4(IP: str):
                string = IP.split(".")

                for s in string:
                    if len(s) == 0 or len(s) > 3:
                        return "Neither"
                    if not s.isdigit():
                        return "Neither"
                    if s[0] == "0" and len(s) != 1:
                        return "Neither"
                    if int(s) > 255:
                        return "Neither"

                return "IPv4"
            return validateIPv4(IP)

        elif IP.count(":") == 7:
            def validateIPv6(IP: str):
                string = IP.split(":")
                hexadigit = '0123456789abcdefABCDEF'
                for s in string:
                    if len(s) == 0 or len(s) > 4:
                        return "Neither"
                    for c in s:
                        if c not in hexadigit:
                            return "Neither"
                return "IPv6"
            return validateIPv6(IP)
        return "Neither"

sol = Solution()
print(sol.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))
print(sol.validIPAddress("172.16.254.1"))
print(sol.validIPAddress("172.16.254.01"))
print(sol.validIPAddress("172.16.254.a0"))
print(sol.validIPAddress("256.256.256.256"))
print(sol.validIPAddress("2001:0db8:85a3::8A2E:0370:7334"))
print(sol.validIPAddress("02001:0db8:85a3:0000:0000:8a2e:0370:7334"))
