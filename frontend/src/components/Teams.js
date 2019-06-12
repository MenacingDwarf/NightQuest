import React, {Component} from 'react'
import TeamsList from "./TeamsList";
import InvitesList from "./InvitesList";
import NewTeam from "./NewTeam";

class Teams extends Component {
    state = {
        teams: null,
        invites: null,
        creating: false
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
                teams: answer.teams_list,
                invites: answer.invites_list
            })
        };
        xhr.send()
    };

    render() {
        let new_team = this.state.creating ? (
            <NewTeam/>
        ) : null;
        let new_button_text = this.state.creating ? "Закрыть" : "Новая команда";
        return (
            <div className="row">
                <div className="col-7">
                    <div style={{marginBottom: "0.25em"}}>
                        <h4 style={{display: "inline"}}>СПИСОК ВАШИХ КОМАНД</h4>
                        <span className="new_team-button" onClick={() => this.setState({creating: !this.state.creating})}>
                            {new_button_text}
                            </span>
                    </div>
                    <div className="line"/>
                    {new_team}
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