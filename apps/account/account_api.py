#-*-coding=utf-8-*-

from libs.db import db

class AccountApi(db.BaseDB):
    
    def __init__(self, user=None):
        self.response_data = {"status": 0, "message": "成功"}
        self.user = user
    
    def get_accounts(self):
        account_info_list = []
        try:
            self.conn()
            sql_str = '''SELECT A.ID, Description, Amount, Time, UserLv, UserYu, UserXu, U.first_name, EditDate
                        FROM account_info A
                        LEFT JOIN auth_user U ON U.id=A.Operator
                        ORDER BY EditDate DESC
                        LIMIT %s,%s
                        '''
            self.cursor.execute(sql_str, (0, 50, ))
            for account_id, desc, amount, time, lv, yu, xu, operator, edit_time in self.fetchall():
                account_info_list.append({
                    "account_id": account_id,
                    "desc": desc,
                    "amount": amount,
                    "time": time,
                    "lv": lv,
                    "yu": yu,
                    "xu": xu,
                    "operator": operator,
                    "edit_time": edit_time,
                })
        finally:
            self.close()
        return account_info_list
    
    def get_present(self):
        presents = {}
        try:
            self.conn()
            sql_str = '''SELECT U.last_name, Amount
                        FROM account_present P
                        LEFT JOIN auth_user U ON U.id=P.UserID
                        '''
            self.cursor.execute(sql_str)
            for name, amount in self.fetchall():
                presents[name] = amount
        finally:
            self.close()
        return presents
    
    def keep_account(self, data):
        account = self._parse_account(data, self.user.last_name)
        try:
            self.conn()
            sql_str = '''INSERT INTO account_info 
                        (Description, Amount, Time, UserLv, UserYu, UserXu, Operator) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                        '''
            self.cursor.execute(sql_str, (
                data["description"], data["amount"], data["time"],
                account["lv"], account["yu"], account["xu"], self.user.id))
            for i in account:
                self._update_wealth(account[i], i)
        finally:
            self.close()
        return self.response_data
    
    def _parse_account(self, data, user):
        account = {
            "lv": float("-" + data["amount_1"]),
            "yu": float("-" + data["amount_2"]),
            "xu": float("-" + data["amount_3"]),
        }
        account[user] = account[user] - account["lv"] - account["yu"] - account["xu"]
        return account
    
    def _update_wealth(self, amount, name):
        sql_str = '''UPDATE account_present P
                    LEFT JOIN auth_user U ON U.id=P.UserID
                    SET Amount=Amount+%s WHERE U.last_name=%s
                    '''
        self.cursor.execute(sql_str, (amount, name, ))
        return 0