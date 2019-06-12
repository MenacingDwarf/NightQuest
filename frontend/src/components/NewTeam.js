import React, {Component} from 'react'

class NewTeam extends Component {
    render() {
        return (
            <form action="teams/add/team" method="post">
                <label className="d-block" htmlFor="title">Название команды</label>
                <input type="text" id="title" placeholder="Название команды"
                       name="title"/>
                <input type="submit" className="register-button" value="Создать"/>
                <div className="line"/>
            </form>
        )
    }
}

export default NewTeam