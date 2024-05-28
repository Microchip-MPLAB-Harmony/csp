import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import { useState } from 'react';
import { Button } from 'primereact/button';
import PeripheralsConfiguration from './PeripheralsConfiguration';
import { Dialog } from 'primereact/dialog';
import GenericClockConfiguration from './GenericClockConfiguration';

const PeripheralClockControllerBox = (props: {
  clockController: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const [periPheralPopup, setPeriPheralPopup] = useState(false);
  const [genericPopup, setGenericPopup] = useState(false);

  return (
    <div>
      <Button
        label='Peripheral Clock Configuration'
        className={props.cx('btn_pclk_config')}
        onClick={() => setPeriPheralPopup(true)}
      />
      <Button
        label='Generic Clock Configuration'
        className={props.cx('btn_pclk_generic')}
        onClick={() => setGenericPopup(true)}
      />
      <Dialog
        header='Peripheral Clock Configuration'
        visible={periPheralPopup}
        maximizable={true}
        onHide={() => {
          setPeriPheralPopup(false);
        }}>
        <PeripheralsConfiguration />
      </Dialog>
      <Dialog
        header='Generic Clock Configuration'
        visible={genericPopup}
        maximizable={true}
        onHide={() => {
          setGenericPopup(false);
        }}>
        <GenericClockConfiguration />
      </Dialog>
    </div>
  );
};

export default PeripheralClockControllerBox;
