import { Row, Col, ListGroup, Button, Modal, Form } from '@blueupcode/components'
import React, { useEffect } from 'react';
import { Controller } from 'react-hook-form'
import DateTimePicker from 'react-datetime'

// Don't forget the CSS: core and the UI components + plugins you are using.
import '@uppy/core/dist/style.min.css';
import '@uppy/dashboard/dist/style.min.css';
import { DATETIME_FORMAT, DATE_FORMAT, TIME_FORMAT, NUMBER_ARRAY_10, ALLOW_FILE_TYPES } from 'constant/const';

type Props = {
  configData: any,
  control: any,
  handleFolderSelection?: (event: React.ChangeEvent<HTMLInputElement>, key: string) => void,
  onChangeSelect?: (id: string, key: string) => void,
  data: any,
} 

export const InputForm1 = (props: Props) => {
  const [serverErrors, setServerErrors] = React.useState<any>({});
  const {
    configData,
    control,
    handleFolderSelection,
    onChangeSelect,
    data
  } = props;

	return (
    <>
      {Object.keys(configData).map(key => {
        const config = configData[key];
        switch(config.type) {
          case 'file':
            return (
              <Controller
                key={key}
                name={key}
                control={control}
                render={({ field, fieldState: { invalid, error } }) => (
                  <Form.Group controlId={key}>
                    <Row className='mt-2'>
                      <Col sm={12}>
                        <div className='d-flex align-items-center'>
                          <Form.Label className='w-sm mb-0'>{`${config.display_name} ${config.require===true?'*':''}:`}</Form.Label>
                          <div className={config.classNames ?? 'fr-1'}>
                            <Form.Control
                              disabled={config.readonly ?? false}
                              type='text'
                              // disabled={readOnly}
                              isInvalid={invalid || !!serverErrors[key]}
                              {...field}
                            />
                            {invalid && <Form.Control.Feedback type="invalid">{error?.message}</Form.Control.Feedback>}
                            {!!serverErrors[key] && <Form.Control.Feedback type="invalid">{serverErrors[key]}</Form.Control.Feedback>}
                          </div>
                          {config.extra_data?.type !== 'auto' && 
                            <div className='align-self-start'>
                              <label htmlFor="forderInput" className='btn btn-success ms-2'>Duyệt thư mục</label>
                              <input
                                type="file"
                                id="forderInput"
                                onChange={(e) => {
                                  if (handleFolderSelection) {
                                    handleFolderSelection(e, key);
                                  }
                                }}
                                accept={config.allow_file_type ?? null}
                                hidden
                                webkitdirectory="true"
                                // directory
                                multiple
                              />
                            </div>
                          }
                        </div>
                      </Col>
                    </Row>
                  </Form.Group>
                )}
              />
            );
          case 'select':
            const selected_list = props.data[config.selected_list];
            return (
              <Controller
                key={key}
                name={key}
                control={control}
                render={({ field, fieldState: { invalid, error } }) => (
                  <Form.Group controlId={key}>
                    <Row className='mt-2'>
                      <Col sm={12}>
                        <div className='d-flex align-items-center'>
                        <Form.Label className='w-sm mb-0'>{`${config.display_name} ${config.require===true?'*':''}:`}</Form.Label>
                        <div className={config.classNames ?? 'fr-1'}>
                            <Form.Select
                              disabled={config.readonly ?? false}
                              // defaultValue=""
                              {...field}
                              onChange={(e) => {
                                field.onChange(e);
                                if (onChangeSelect) {
                                  onChangeSelect(e.target.value, key);
                                }
                              }}
                            >
                              <option value=""></option>
                              {Object.keys(selected_list).map((k: string) => (
                                <option key={k} value={k} selected={config.default_value && k==config.default_value}>{selected_list[k].name}</option>
                              ))}
                            </Form.Select>
                            {invalid && <Form.Control.Feedback type="invalid">{error?.message}</Form.Control.Feedback>}
                            {!!serverErrors[key] && <Form.Control.Feedback type="invalid">{serverErrors[key]}</Form.Control.Feedback>}
                          </div>
                        </div>
                      </Col>
                    </Row>
                  </Form.Group>
                )}
              />
            );
          case 'textarea':
            return (
              <Controller
                key={key}
                name={key}
                control={control}
                render={({ field, fieldState: { invalid, error } }) => (
                  <Form.Group controlId={key}>
                    <Row className='mt-2'>
                      <Col sm={12}>
                        <div className='d-flex align-items-center'>
                          <Form.Label className='w-sm mb-0'>{`${config.display_name} ${config.require===true?'*':''}:`}</Form.Label>
                          <div className={config.classNames ?? 'fr-1'}>
                            <Form.Control
                              disabled={config.readonly ?? false}
                              as="textarea"
                              // type={config.type ?? 'text'}
                              isInvalid={invalid || !!serverErrors[key]}
                              {...field}
                            />
                            {invalid && <Form.Control.Feedback type="invalid">{error?.message}</Form.Control.Feedback>}
                            {!!serverErrors[key] && <Form.Control.Feedback type="invalid">{serverErrors[key]}</Form.Control.Feedback>}
                          </div>
                        </div>
                      </Col>
                    </Row>
                  </Form.Group>
                )}
              />
            );
          case 'timepicker':
            return (
              <Controller
                key={key}
                name={key}
                control={control}
                render={({ field, fieldState: { invalid, error } }) => (
                  <Form.Group controlId={key}>
                    <Row className='mt-2'>
                      <Col sm={12}>
                        <div className='d-flex align-items-center'>
                          <Form.Label className='w-sm mb-0'>{`${config.display_name} ${config.require===true?'*':''}:`}</Form.Label>
                          <div className={config.classNames ?? 'fr-1'}>
                          <DateTimePicker
                            closeOnSelect
                            dateFormat={false}
                            timeFormat={TIME_FORMAT}
                            onChange={(date) => field.onChange(date)}
                            value={field.value}
                            initialViewMode={'time'}
                          />
                          {invalid && <Form.Control.Feedback type="invalid">{error?.message}</Form.Control.Feedback>}
                          {!!serverErrors[key] && <Form.Control.Feedback type="invalid">{serverErrors[key]}</Form.Control.Feedback>}
                          </div>
                        </div>
                      </Col>
                    </Row>
                  </Form.Group>
                )}
              />
            );
          case 'number':
            return (
              <Controller
                key={key}
                name={key}
                control={control}
                render={({ field, fieldState: { invalid, error } }) => (
                  <Form.Group controlId={key}>
                    <Row className='mt-2'>
                      <Col sm={12}>
                        <div className='d-flex align-items-center'>
                          <Form.Label className='w-sm mb-0'>{`${config.display_name} ${config.require===true?'*':''}:`}</Form.Label>
                          <div className={config.classNames ?? 'fr-1'}>
                            <Form.Control
                              disabled={config.readonly ?? false}
                              type='number'
                              isInvalid={invalid || !!serverErrors[key]}
                              min={config.min}
                              max={config.max}
                              {...field}
                            />
                            {invalid && <Form.Control.Feedback type="invalid">{error?.message}</Form.Control.Feedback>}
                            {!!serverErrors[key] && <Form.Control.Feedback type="invalid">{serverErrors[key]}</Form.Control.Feedback>}
                          </div>
                          {config.post_display && (
                            <div className='ms-2'>{config.post_display}</div>
                          )}
                        </div>
                      </Col>
                    </Row>
                  </Form.Group>
                )}
              />
            );
          default:
            return (
              <Controller
                key={key}
                name={key}
                control={control}
                render={({ field, fieldState: { invalid, error } }) => (
                  <Form.Group controlId={key}>
                    <Row className='mt-2'>
                      <Col sm={12}>
                        <div className='d-flex align-items-center'>
                          <Form.Label className='w-sm mb-0'>{`${config.display_name} ${config.require===true?'*':''}:`}</Form.Label>
                          <div className={config.classNames ?? 'fr-1'}>
                            <Form.Control
                              disabled={config.readonly ?? false}
                              type={config.type ?? 'text'}
                              isInvalid={invalid || !!serverErrors[key]}
                              {...field}
                            />
                            {invalid && <Form.Control.Feedback type="invalid">{error?.message}</Form.Control.Feedback>}
                            {!!serverErrors[key] && <Form.Control.Feedback type="invalid">{serverErrors[key]}</Form.Control.Feedback>}
                          </div>
                          {config.post_display && (
                            <div className='ms-2'>{config.post_display}</div>
                          )}
                        </div>
                      </Col>
                    </Row>
                  </Form.Group>
                )}
              />
            );
        }
      })}
    </>
  )
}
