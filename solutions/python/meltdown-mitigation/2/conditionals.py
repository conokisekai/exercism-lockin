def is_criticality_balanced(temperature, neutrons_emitted):
    if temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000:
        return True
    else:
        return False


def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    efficiency = (generated_power/theoretical_max_power)*100
    if efficiency >= 80:
        say = "green"
    elif efficiency >= 60:
        say = "orange"
    elif efficiency >= 30:
        say = "red"
    else :
        say = "black"
    return say


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    result = temperature * neutrons_produced_per_second
    if result < (0.9 * threshold):
        say = "LOW"
    elif (0.9 * threshold) <= result <= (1.1 * threshold):
        say = "NORMAL"
    else:
        say = "DANGER"
    return say 