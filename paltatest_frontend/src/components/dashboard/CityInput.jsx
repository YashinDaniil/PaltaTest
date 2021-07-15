import React, {useState} from 'react'
import axios from 'axios';
import {Button, Alert, Dropdown, DropdownButton} from 'react-bootstrap';
import { AddressSuggestions } from 'react-dadata';
import 'react-dadata/dist/react-dadata.css';

const CityInput = (props) => {
	const [data, setData] = useState(null)
	const [alertState, setAlertState] = useState(false)
	const [taskData, setTaskData] = useState(null)

	function disableAlert() {
		setAlertState(false)
	}

	function SetCity() {
		if (taskData !== null) {
			setAlertState(true)

			setTimeout(disableAlert, 5000)
		} else {
			props.clearGraph()
			axios({
				method: 'post',
				url: ''.concat(process.env.REACT_APP_API_URL_HOST, '/api/v1/weather/set_position'),
				headers: {
					'Content-Type': 'application/json',
					'Accept': '*/*',
					'User_ID': localStorage.getItem('user_id'),

				},
				data: {
					city: data.value,
				}
			})
				.then(function (res) {
					setTaskData(res.data.task_id)
				})
				.catch(function (res) {
					console.log(res)
				})
		}
	}

	function revokeTask(){
		axios({
				method: 'post',
				url: ''.concat(process.env.REACT_APP_API_URL_HOST, '/api/v1/weather/revoke_task'),
				headers: {
					'Content-Type': 'application/json',
					'Accept': '*/*',

				},
				data: {
					task_id: taskData,
				}
			})
				.then(function (res) {
					setTaskData(null)
					props.clearGraph()
				})
				.catch(function (res) {
					console.log(res)
				})
	}
	const numbers = Object.keys(props.dropdown);
		const listItems = numbers.map((city) =>
            <Dropdown.Item eventKey={city} onClick={()=>props.updateSelectDropdown({city})}>{city}</Dropdown.Item>
	);

	return (
		<div className={'container mt-50'}>
			<Alert key={'danger'} variant={'danger'} show={alertState}>
					Город уже выбран, пожалуйста уберите задачу
            </Alert>
			<div className={'row'}>
				<div className={'col-6'}><AddressSuggestions token={process.env.REACT_APP_DADATA_TOKEN} value={data} onChange={setData} /></div>
				<div className={'col-5 offset-1'}>
					<Button onClick={SetCity} size="sm" className={'header_button'}>Выбрать город</Button>
					<Button onClick={revokeTask} size="sm" variant="danger" className={'header_button'}>Убрать задачу</Button>
				</div>
			</div>

			<div className={'mt-20'}>
				<DropdownButton id="dropdown-basic-button" title="Dropdown button">
				{listItems}
			</DropdownButton>
			</div>


		</div>
	)
}

export default CityInput