import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import { useState } from 'react';
import { Button } from 'primereact/button';
import GclockIOConfiguration from './GclockIOConfiguration';
import { Dialog } from 'primereact/dialog';
import PeripheralClockConfiguration from './PeripheralClockConfiguration';

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
        className={props.cx('periClockConfig')}
        onClick={() => setPeriPheralPopup(true)}
      />
      <Button
        label='GCLK I/O Configuration'
        className={props.cx('gclkIOConfig')}
        onClick={() => setGenericPopup(true)}
      />
      <Dialog
        header='Peripheral Clock Configuration'
        visible={periPheralPopup}
        maximizable={true}
        onHide={() => {
          setPeriPheralPopup(false);
        }}>
        <PeripheralClockConfiguration />
      </Dialog>
      <Dialog
        header='GCLK I/O Configuration'
        visible={genericPopup}
        maximizable={true}
        onHide={() => {
          setGenericPopup(false);
        }}>
        <GclockIOConfiguration />
      </Dialog>
    </div>
  );
};

export default PeripheralClockControllerBox;
