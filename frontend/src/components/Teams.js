import React, {Component} from 'react'
import TeamsList from "./TeamsList";
import InvitesList from "./InvitesList";

class Teams extends Component {
    state = {
        teams: null,
        invites: null
    };

    componentDidMount() {
        let comp = this;
        let xhr = new XMLHttpRequest();
        xhr.open("GET", '/teams_info', true);
        xhr.onreadystatechange = function () {
            if (this.readyState !== 4) return;
            let answer = JSON.parse(this.responseText);
            console.log(answer);
            comp.setState({
                teams: JSON.parse(answer.teams_list),
                invites: JSON.parse(answer.invites_list)
            })
        };
        xhr.send()
    };
    render() {
        return (
            <div className="row">
                <div className="col-7">
                    <div style={{marginBottom: "0.25em"}}>
                        <h4 style={{display: "inline"}}>СПИСОК ВАШИХ КОМАНД</h4>
                        <span className="new_team-button">Новая команда</span>
                    </div>
                    <div className="line"/>
                    <TeamsList teams={this.state.teams}/>
                </div>
                <div className="col-5">
                    <h4>ПРИГЛАШЕНИЯ В КОМАНДУ</h4>
                    <div className="line"/>
                    <InvitesList invites={this.state.invites}/>
                </div>
            </div>
        )
    }
}

export default Teams