import React, {Component} from 'react'
import logo from '../NQlogo.png';

class App extends Component {
    render() {
        return (
            <div className="wrap">
                <div className="header">
                    <div className="logo">
                        <img src={logo} alt="картинка"/>
                    </div>
                    <ul className="buttons">
                        <li>
                            <div className="button">button1</div>
                            <div className="underline"></div>
                        </li>
                        <li>
                            <div className="button">button2</div>
                            <div className="underline"></div>
                        </li>
                        <li>
                            <div className="button">button3</div>
                            <div className="underline"></div>
                        </li>
                    </ul>
                </div>
            </div>

        )
    }
}

export default App;
