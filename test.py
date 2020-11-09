from collections import defaultdict
import queue

t = {
    "q0": {"0" : ("q1", "zero"), "2":("q2","vinte"), "3":("q2","trinta"), "4":("q2","quarenta"), "5":("q2","cinquenta"), "6":("q2","sessenta"), "7":("q2","setenta"), 
               "8":("q2","oitenta"), "9":("q2","noventa"), "10":("q2", "cem"), "20":("q2", "duzentos"), "30":("q2", "trezentos"), "40":("q2", "quatrossentos"),
                "50":("q2", "quinhentos"), "60":("q2", "seiscentos"), "70":("q2","setessentos"), "80":("q2","oitossentos"),  "90":("q2", "novessentos")},    
    
    "q1": {"0" : ("q0", "") },
    
    "q2": {"0" : ("q3", ""), "1" : ("q3", "e um"), "2" : ("q3", "e dois"), "3" : ("q3", "e três"), "4" : ("q3", "e quatro"), "5" : ("q3", "e cinco"), "6" : ("q3", "e seis"), 
               "7" : ("q3", "e sete"), "8" : ("q3", "e oito"), "9" : ("q3", "e nove"),},
    
    "q3": { }
}

def run(number):
    qcurrent="q0"
    out=""
    num = ""
    for n in number:
        num += n
        if num in t[qcurrent]:
            qcurrent, output = t[qcurrent][num]
            out=out+ ' ' +output
            if num.startswith("1"):
                num = ""
        elif num in t["q0"]:
            qcurrent, output = t["q0"][num]
            out=output
            num = ""
            

    print(out)

run("706")
