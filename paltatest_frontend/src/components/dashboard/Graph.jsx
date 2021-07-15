import {
  LineChart, XAxis, Tooltip, CartesianGrid, Line, YAxis
} from 'recharts';

function WeatherGraph(props) {

	return (
		<div>
			<LineChart
				width={1000}
				height={400}
				data={props.data}
				margin={{top: 50, right: 20, left: 50, bottom: 5}}
			>

				<XAxis dataKey="name"/>
				<YAxis/>
				<Tooltip/>
				<CartesianGrid stroke="#f5f5f5"/>
				<Line type="monotone" dataKey="Температура"  stroke="#ff7300" activeDot={{r: 5}}/>
				<Line type="monotone" dataKey="Ощущается как"  stroke="#ff7350" activeDot={{r: 5}}/>

			</LineChart>
		</div>
	)
}

export default WeatherGraph