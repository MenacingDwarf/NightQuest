import React, {Component} from 'react'
import Team from "./Team";

class TeamsList extends Component {

    render() {
        let teams = <div>Загрузка...</div>
        if (this.props.teams !== null) {
            let teams_list = this.props.teams.map(team => (
                <Team team={team} key={team.pk}/>
            ));
            teams = this.props.teams.length > 0 ? (
                <div>
                    {teams_list}
                </div>
            ) : (
                <div>Нет доступных команд</div>
            );
        }
        return (
            <div>
                {teams}
            </div>
        )
    }
}

export default TeamsList