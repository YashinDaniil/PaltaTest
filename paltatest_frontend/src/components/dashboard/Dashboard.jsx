import React, { useEffect, useState } from 'react'
import { w3cwebsocket as W3CWebSocket } from "websocket";
import { v4 as uuidv4 } from 'uuid';
import CityInput from './CityInput'
import WeatherGraph from './Graph'
import '../style/dashboard.css'
import axios from "axios";

const client = new W3CWebSocket(process.env.REACT_APP_WS_URL_HOST);

const Dashboard = () => {
	const [data, setData] = useState([])
	const [dataDropdown, setDropdownData] = useState([])

	function updateGraphData() {
		setData([])
	}

	function updateSelectDropdown(e) {
		setData(dataDropdown[e.city])
	}

	useEffect(() => {
		let user_id = localStorage.getItem('user_id')
		if(user_id === null) {
			localStorage.setItem('user_id', uuidv4())
		}
		const url = ''.concat(process.env.REACT_APP_API_URL_HOST, '/api/v1/weather/get_old_search/', localStorage.getItem('user_id'))
		axios({
				method: 'get',
				url: url
			})
				.then(function (res) {
					setDropdownData(res.data)
				})
				.catch(function (res) {
					console.log(res)
				})

		client.onopen = () => {
			function sendMessage() {
				if (client.readyState === client.OPEN) {
					const mes = localStorage.getItem('user_id')
					client.send(mes)
				}
			}
			sendMessage()
		}
		client.onmessage = (message) => {
			let update_item = (JSON.parse((message.data)).content)
			setData(oldArray => [...oldArray, update_item])
		}
	}, [])

	return (
		<div>
			<CityInput clearGraph={updateGraphData} dropdown={dataDropdown} updateSelectDropdown={updateSelectDropdown}/>
			<WeatherGraph data={data}/>
		</div>
	)
}

export default Dashboard