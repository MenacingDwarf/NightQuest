import React, {Component} from 'react'
import logo from '../NQlogo.png';
import Header from "./Header";

class App extends Component {
    render() {
        return (
            <div className="wrap">
                <div className="blur"/>
                <Header/>
                <h1>Hello</h1>
                <p>Welcome to Night Quest website!</p>
            </div>

        )
    }
}

export default App;
