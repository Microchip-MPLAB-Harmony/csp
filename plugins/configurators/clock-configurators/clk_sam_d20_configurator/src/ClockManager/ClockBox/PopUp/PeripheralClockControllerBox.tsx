import { useState } from 'react';
import { Button } from 'primereact/button';
import GclockIOConfiguration from './GclockIOConfiguration';
import { Dialog } from 'primereact/dialog';
import PeripheralClockConfiguration from './PeripheralClockConfiguration';

const PeripheralClockControllerBox = (props: { cx: (...classNames: string[]) => string }) => {
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
        label='GCLK In/Out Configuration'
        className={props.cx('gclkIOConfiguration')}
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
