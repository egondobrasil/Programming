print("<tr><td>Dia</td>")
hora=8
while hora < 23:
        print(f"<td>{hora}</td>")
        hora+=1
print("</tr>")
dia=1
blanktd="<td>.</td>"
while dia<31:
        print(f"<tr><td>{dia}</td>{blanktd*15}</tr>")
        dia+=1