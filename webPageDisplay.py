f = open('weather.html','w')

message = """
<html>
<head><style>
th { font-size: 120%; }
td { font-size: 110%; }
</style></head>
<body bgcolor="lavender">
<p><h2><center>
<table border="1" width="60%"><caption><h1>Weather Details</h1></caption>
<tr>
<th colspan="2">coord</th>
</tr>
<tr>
<td>lon</td>
<td>145.77</td>
</tr>
<tr>
<td>lat</td>
<td>-16.92</td>
</tr>
<tr>
<th colspan="2">weather</th>
</tr>
<tr>
<td>id</td>
<td>802</td>
</tr>
<tr>
<td>main</td>
<td>Clouds</td>
</tr>
<tr>
<td>description</td>
<td>scattered clouds</td>
</tr>
<tr>
<td>icon</td>
<td>03n</td>
</tr>
<tr>
<th colspan="2">main</th>
</tr>
<tr>
<td>temp</td>
<td>300.15</td>
</tr>
<tr>
<td>pressure</td>
<td>1007</td>
</tr>
<tr>
<td>humidity</td>
<td>74</td>
</tr>
<tr>
<td>temp_min</td>
<td>300.15</td>
</tr>
<tr>
<td>temp_max</td>
<td>300.15</td>
</tr>
<tr>
<th colspan="2">wind</th>
</tr>
<tr>
<td>speed</td>
<td>3.6</td>
</tr>
<tr>
<td>deg</td>
<td>160</td>
</tr>
<tr>
<th colspan="2">clouds</th>
</tr>
<tr>
<td>all</td>
<td>40</td>
</tr>
<tr>
<th colspan="2">sys</th>
</tr>
<tr>
<td>type</td>
<td>1</td>
</tr>
<tr>
<td>id</td>
<td>8166</td>
</tr>
<tr>
<td>message</td>
<td>0.2064</td>
</tr>
<tr>
<td>country</td>
<td>AU</td>
</tr>
<tr>
<td>sunrise</td>
<td>1485720272</td>
</tr>
<tr>
<td>sunset</td>
<td>1485766550</td>
</tr>
<tr>
<th>dt</th>
<th>1485790200</th>
</tr>
<tr>
<th>visibility</th>
<th>10000</th>
</tr>
<tr>
<th>base</th>
<th>stations</th>
</tr>
<tr>
<th>id</th>
<th>2172797</th>
</tr>
<tr>
<th>name</th>
<th>Cairns</th>
</tr>
<tr>
<th>cod</th>
<th>200</th>
</tr>
</table>
</center>
</h2>
</p></body>
</html>
"""

f.write(message)
f.close()