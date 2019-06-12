import React, {Component} from 'react'

class Team extends Component {
    render() {
        let team = this.props.team;
        let members = this.props.team.members.map((member, index) => (
            <li key={index}>{member}</li>
        ));
        return (
            <div className={"team-place"}>
                <a href={"/teams/"+team.id}><h3>{team.title}</h3></a>
                <p><b>Капитан</b>: {team.captain}</p>
                <p><b>Состав команды</b>:</p>
                <ul style={{listStyleType: "none"}}>
                    {members}
                </ul>
            </div>
        )
    }
}

export default Team