import React, {Component} from 'react'
import logo from '../NQlogo.png';
import Header from "./Header";
import { BrowserRouter, Route } from 'react-router-dom'
import Home from "./Home";
import Teams from "./Teams";
import Register from "./Register";

class App extends Component {
    render() {
        return (
            <div className="wrap">
                <BrowserRouter>
                    <div className="blur"/>
                    <Header/>
                    <Route exact path={"/"} component={Home} />
                    <Route path={"/register"} component={Register}/>
                    <Route path={"/login"} component={Register}/>
                </BrowserRouter>
            </div>

        )
    }
}

export default App;
