import decimal

class Precision:
    def __init__(self, prec):
      self.prec = prec 
      self.actual_prec = decimal.getcontext().prec

    def __enter__(self):
        decimal.getcontext().prec = self.prec 
    
    def __exit__(self, exc_type, exc_val, exc_trace):
        decimal.getcontext().prec = self.actual_prec
        return False  # bubble up the exception if any
    

if __name__ == '__main__':
    with Precision(3):
        a = decimal.Decimal(1)
        b = decimal.Decimal(3)

        print(a/b) # 0.333
    print(a/b) # 0.3333333333333333333333333333

    with decimal.localcontext() as ctxt:  # innbuilt method that does same as Precision()
        ctxt.prec = 5
        a = decimal.Decimal(1)
        b = decimal.Decimal(3)

        print(a/b) # 0.33333
    print(a/b) # 0.3333333333333333333333333333