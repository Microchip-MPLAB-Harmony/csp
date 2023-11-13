import { Button } from "primereact/button";
import "./ChannelConfiguration.css";
import ChannelTable from "./ChannelConfigurationTable";
import ChannelSettingsPane from "./ChannelSettingsPane";

const ChannelConfigruation = (props: any) => {
  const getChannelNumber = () => {
    return props.channels.selectedChannel.replace(/^\D+/g, "");
  };

  return (
    <div className="channel_group_config">
      <div className="channel_configuration">
        <div className="channel_configuration__title">
          Channel Configuration
        </div>
        <div>
          <ChannelTable
            channelList={props.channels.channelList}
            selectedChnl={props.channels.selectedChannel}
            channelSelectionChanged={props.onSetSelectedChannel}
            onRemoveChannel={props.onRemoveChannel}
          />
        </div>
        <Button
          className="p-button-raised p-button-rounded align-self-center"
          onClick={(event) => {
            props.onAddChannel(event);
          }}
          disabled={
            props.channels.channelList.length ===
            Number(props.channels.maxChannels)
          }
        >
          Add Channel
        </Button>
      </div>
      <div className="flex flex-column gap-3">
        <div className="channel_configuration__title">
          Channel {getChannelNumber()} Settings
        </div>
        <ChannelSettingsPane channelNum={getChannelNumber()} />
      </div>
    </div>
  );
};

export default ChannelConfigruation;
