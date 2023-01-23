import model as m
import view as v

def start():
    type = v.get_type()
    value_a = v.get_value(type)
    value_b = v.get_value(type)
    operator = v.get_operator(type)
    m.init(value_a, value_b)
    match operator:
        case "-":
            result = m.sub()
        case "+":
            result = m.sum()
        case "*":
            result = m.mult()
        case "/":
            result = m.div()
        case "//":
            result = m.divv()
        case "%":
            result = m.mod()    
    v.view_data(result, "result")