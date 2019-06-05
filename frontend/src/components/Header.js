import React, {Component} from 'react'
import logo from "../NQlogo.png";
import HeaderButtons from "./HeaderButtons";

class Header extends Component {
    render() {
        let hello = this.props.user_info ? (
            <div className="hello">
                Добро пожаловать, {this.props.user_info.username}
            </div>
        ) : null;
        return (
            <header className="header">
                <div className="logo">
                    <img src={logo} alt="картинка"/>
                </div>
                <div className="header-right">
                    <HeaderButtons {...this.props} />
                    <div className="header-text">
                        {hello}
                        Night Quest...
                    </div>
                </div>
            </header>
        )
    }
}

export default Header