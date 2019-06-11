import React, {Component} from 'react'

class Team extends Component {
    render() {
        let team = this.props.team;
        return (
            <div>
                <h3>{team.fields.title}</h3>
                Капитан: {team.fields.captain}
                <div className="line"/>
            </div>
        )
    }
}

export default Team