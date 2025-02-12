import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import {useState } from 'react';
import { Button } from 'primereact/button';
import { Dialog } from 'primereact/dialog';
import GenericClockConfig from './GenericClockConfig';

const GenericClockConfigBox = (props: {
  clockController: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const [periPheralPopup, setPeriPheralPopup] = useState(false);

  return (
    <div>
      <Button
        label='Generic Clock Configuration'
        className={props.cx('gclockConfig')}
        onClick={() => setPeriPheralPopup(true)}
      />
      <Dialog
        header='Generic Clock Configuration'
        visible={periPheralPopup}
        maximizable={true}
        onHide={() => {
          setPeriPheralPopup(false);
        }}>
        <GenericClockConfig />
      </Dialog>
    </div>
  );
};

export default GenericClockConfigBox;
