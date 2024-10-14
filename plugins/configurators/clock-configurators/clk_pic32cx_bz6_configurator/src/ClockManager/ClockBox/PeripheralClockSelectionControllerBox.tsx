import { GetButton } from 'clock-common/lib/Components/NodeType';

const PeripheralClockSelectionControllerBox = () => {
  function PeripheralClockConfigurationButtonClicked() {
    // callPopUp(GenericPopUp, peripheralClockConfig_PopupHeadding, '40vw', '95vh');
  }
  return (
    <div>
      <GetButton
        buttonDisplayText={'Peripheral Configuration'}
        className={'periClockConfig'}
        toolTip={'click to configure Peripheral Clock parameters'}
        buttonClick={PeripheralClockConfigurationButtonClicked}
      />
    </div>
  );
};
export default PeripheralClockSelectionControllerBox;
