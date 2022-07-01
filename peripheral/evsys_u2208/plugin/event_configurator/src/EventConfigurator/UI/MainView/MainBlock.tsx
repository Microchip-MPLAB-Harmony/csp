import Header from "./ToolBar";
import {
  SetComponentId,
  clearSymbol,
  UpdateSymbolValue,
} from "../../../Common/SymbolAccess";
import { globalSymbolSStateData } from "../../../Common/UIComponents/UIComponentCommonUtils";
import { convertToBoolean } from "../../../Common/Utils";
import ChannelConfigruation from "./ChannelConfiguration";
import {
  addUser,
  enableDisableChannel,
  enableNextAvailableChannel,
  getEnabledChannelList,
  GetMaxChannels,
  GetUsersData,
  registerForUsersUpdateCallback,
} from "../../EventService";
import UserConfigruation from "./UserConfiguration";
import "./MainBlock.css";
import {
  ChangeClassNameState,
  ChangeComponentState,
} from "Common/UIComponents/StateChangeUtils";
import { useState } from "react";
import { registerForChannelUpdateCallback } from "../../EventService";
import { Dialog } from "primereact/dialog";
import { Button } from "primereact/button";

export let progressStatus = true;

export let component_id = "evsys";
export let toolBarHeight = "60px";

const MainBlock = () => {
  SetComponentId(component_id);
  registerForChannelUpdateCallback();
  registerForUsersUpdateCallback();

  const [channels, setChannels] = useState<{
    channelList: string[];
    selectedChannel: string;
    maxChannels: number;
  }>({
    channelList: getEnabledChannelList(),
    selectedChannel: "",
    maxChannels: GetMaxChannels(),
  });

  const [displayChannelLocked, setDisplayChannelLocked] =
    useState<boolean>(false);

  const [users, setUsers] = useState<
    { symId: string; key: string; chnl: string }[]
  >(GetUsersData());

  (window as any).SymbolValueChanged = (value: any) => {
    if (value !== null && value !== undefined) {
      const symbolData = value.split("M*C");
      const symbolId: string = symbolData[0];
      const symbolValue = symbolData[1];
      const readOnlyStatus = convertToBoolean(symbolData[2]);
      const visibleStatus = convertToBoolean(symbolData[3]);

      alert("symbolData " + symbolData);
      if (globalSymbolSStateData.get(symbolId) != null) {
        // ChangeValueState(symbolId, symbolValue);
        ChangeComponentState(
          symbolId,
          symbolValue,
          readOnlyStatus,
          visibleStatus
        );
      }

      checkChannelsUpdate(symbolId);
      checkUsersUpdate(symbolId);

      if (symbolId.includes("_NONSEC_")) {
        ChangeClassNameState(symbolId, GetTrustZoneClassName(symbolValue));
      }
    }
  };

  function GetTrustZoneClassName(value: any) {
    if (value === "SECURE") {
      return "secure";
    }
    return "nonsecure";
  }

  const checkChannelsUpdate = (symbolId: string) => {
    let pattern = /EVSYS_CHANNEL_[0-9]+$/;
    if (pattern.test(symbolId)) {
      setChannels((prevState) => {
        return {
          ...prevState,
          channelList: getEnabledChannelList(),
        };
      });
    }
  };

  const checkUsersUpdate = (symbolId: string) => {
    let pattern = /EVSYS_USER_[0-9]+$/;
    if (pattern.test(symbolId)) {
      console.log("User symbol updated " + symbolId);
      setUsers(GetUsersData());
    }
  };

  const addChannel = (event: any) => {
    enableNextAvailableChannel();
    setChannels((prevState) => {
      return {
        ...prevState,
        channelList: getEnabledChannelList(),
      };
    });
  };

  function checkIfChannelIsUsed(chnl: string) {
    return GetUsersData()
      .map((item) => item.chnl)
      .includes(chnl);
  }

  const removeChannel = (chnl: string) => {
    if (channels.channelList.includes(chnl)) {
      if (checkIfChannelIsUsed(chnl)) {
        setDisplayChannelLocked(true);
        return;
      }
      setChannels((prevState) => {
        const index = prevState.channelList.indexOf(chnl);
        const channelList = prevState.channelList;
        channelList.splice(index, 1);
        let newIndex = index + 1;
        if (newIndex >= channelList.length) {
          newIndex = channelList.length - 1;
        }
        let selectedChnl = "";
        if (newIndex !== -1) {
          selectedChnl = channelList[newIndex];
        }
        return {
          channelList: channelList,
          selectedChannel: selectedChnl,
          maxChannels: prevState.maxChannels,
        };
      });
      enableDisableChannel(chnl, false);
      let chnlNum: string = chnl.replace(/^\D+/g, "");
      clearSymbol(component_id, "EVSYS_CHANNEL_" + chnlNum);
    }
  };

  const setSelectedChannel = (chnl: string) => {
    if (channels.channelList.includes(chnl)) {
      setChannels((prevState) => {
        return { ...prevState, selectedChannel: chnl };
      });
    }
  };

  const addNewUser = () => {
    if (addUser()) {
      setUsers(GetUsersData());
    }
  };

  const removeUserFromTable = (sym: string) => {
    UpdateSymbolValue(component_id, sym, "NONE");
    clearSymbol(component_id, sym);
    setUsers(GetUsersData());
  };

  const refreshData = () => {
    setUsers(() => GetUsersData());
  };

  const onHide = () => {
    setDisplayChannelLocked(false);
  };

  const renderFooter = () => {
    return (
      <div>
        <Button label="Ok" onClick={() => onHide()} className="p-button-text" />
      </div>
    );
  };

  return (
    <div>
      <Header />
      <div className="main_view">
        <ChannelConfigruation
          channels={channels}
          onAddChannel={addChannel}
          onRemoveChannel={removeChannel}
          onSetSelectedChannel={setSelectedChannel}
        />
        <div className="dialog">
          <Dialog
            header="Channel Locked"
            visible={displayChannelLocked}
            style={{ width: "50vw" }}
            footer={renderFooter()}
            onHide={() => onHide()}
          >
            <p>Not able to remove channel. This channel is locked by user.</p>
          </Dialog>
        </div>

        <UserConfigruation
          usersList={users}
          addUser={addNewUser}
          removeUser={removeUserFromTable}
          tableDataUpdated={refreshData}
        />
      </div>
    </div>
  );
};

export default MainBlock;
