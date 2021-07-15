import './App.css';
import {BrowserRouter as   Switch, Route} from 'react-router-dom';
import Dashboard from "./components/dashboard/Dashboard";
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  return (
  	<Switch>
	    <Route exact path='/' component={Dashboard} />
    </Switch>
  );
}

export default App;
