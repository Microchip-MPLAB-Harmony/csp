import MultipleComponents from '../Components/MultipleComponents';
// import AddMultipleFields from "Common/AddMultipleUIComponentsWithLabel";
// import MultipleComponents from '@mplab_harmony/harmony-plugin-ui/build/utils/AddMultipleUIComponentsWithLabel';

import { component_id } from './MainBlock';

const ChannelSettingsPane = (props: { channelNum: string }) => {
  const symbols: string[] = [
    'EVSYS_CHANNEL_' + props.channelNum + '_PATH',
    'EVSYS_CHANNEL_' + props.channelNum + '_EDGE',
    'EVSYS_CHANNEL_' + props.channelNum + '_ONDEMAND',
    'EVSYS_CHANNEL_' + props.channelNum + '_RUNSTANDBY',
    'EVSYS_CHANNEL_' + props.channelNum + '_EVENT',
    'EVSYS_CHANNEL_' + props.channelNum + '_OVERRUN',
  ];

  const updateSettingsPane = () => {};

  const getSettingsItems = () => {
    if (props.channelNum === '') {
      return (
        <b>
          Select the channel from Channel Configuration Table to view channel
          settings
        </b>
      );
    } else {
      return (
        <MultipleComponents
          componentId={component_id}
          parentUpdate={updateSettingsPane}
          symbolsArray={symbols}
        />
      );
    }
  };

  return getSettingsItems();
};

export default ChannelSettingsPane;
