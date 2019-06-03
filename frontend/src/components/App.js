import React, {Component} from 'react'
import logo from '../NQlogo.png';
import Header from "./Header";
import { BrowserRouter, Route } from 'react-router-dom'
import Home from "./Home";
import Teams from "./Teams";
import Register from "./Register";
import PersonalArea from "./PersonalArea";

class App extends Component {
    state = {
        is_auth: null,
        user_info: null,
    };
    componentDidMount() {
        let comp = this;
        let xhr = new XMLHttpRequest();
        xhr.open("GET", '/user_info', true);
        xhr.onreadystatechange = function () {
            if (this.readyState !== 4) return;
            let answer = JSON.parse(this.responseText);
            comp.setState({
                is_auth: answer.is_auth,
                user_info: answer.user_info
            })
        };
        xhr.send()
    }
    render() {
        return (
            <div className="wrap">
                <BrowserRouter>
                    <div className="blur"/>
                    <Route path={"/"} render={(routeProps) => (
                        <Header {...routeProps} is_auth={this.state.is_auth} />
                    )} />
                    <Route exact path={"/"} component={Home} />
                    <Route path={"/register"} component={Register}/>
                    <Route path={"/login"} component={Register}/>
                    <Route path={"/personal_area"} component={PersonalArea}/>
                </BrowserRouter>
            </div>

        )
    }
}

export default App;
