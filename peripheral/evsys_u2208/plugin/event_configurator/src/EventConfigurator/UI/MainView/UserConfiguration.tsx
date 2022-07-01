import { Button } from "primereact/button";
import "./UserConfiguration.css";
import UserTable from "./UserConfigurationTable";

const UserConfiguration = (props: {
  usersList: { symId: string; key: string; chnl: string }[];
  addUser: () => void;
  removeUser: (sym: string) => void;
  tableDataUpdated: () => void;
}) => {
  return (
    <div className="user_configuration_group">
      <div className="user_configuration">
        <div className="user_configuration__title">User Configuration</div>
        <div>
          <UserTable
            userData={props.usersList}
            onRemoveUser={props.removeUser}
            onTableDataUpdate={props.tableDataUpdated}
          />
        </div>
        <Button
          className="p-button-raised p-button-rounded"
          onClick={props.addUser}
        >
          Add User
        </Button>
      </div>
    </div>
  );
};

export default UserConfiguration;
