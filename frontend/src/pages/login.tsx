import React from 'react'
import { Row, Col, Portlet, Form, Button, Spinner, Widget12 } from '@blueupcode/components'
import { useForm, Controller } from 'react-hook-form'
import { yupResolver } from '@hookform/resolvers/yup'
import { swal } from 'components/sweetalert2/instance'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faUserAlt } from '@fortawesome/free-solid-svg-icons'
import * as yup from 'yup'
import Link from 'next/link'
import withGuest from 'components/auth/withGuest'
import type { ExtendedNextPage } from '@blueupcode/components/types'

import { useDispatch, useSelector } from "react-redux";
import { ALoginSuccess } from "../store/auth/actions";
import { postLogin } from 'store/request/auth'
import { isSuccessRequest, isInvalid } from 'store/request/helper';
import { AShowLoading, AHideLoading } from 'store/common/actions'
import { getSLoading } from "store/common/selectors";


const LoginPage: ExtendedNextPage = () => {
	return (
		<Row className="g-0 align-items-center justify-content-center h-100">
			<Col sm={8} md={6} lg={4} xl={3}>
				{/* BEGIN Portlet */}
				<Portlet>
					<Portlet.Body>
						<div className="text-center mt-4 mb-5">
							{/* BEGIN Avatar */}
							<Widget12 circle display variant="label-primary">
								<FontAwesomeIcon icon={faUserAlt} />
							</Widget12>
							{/* END Avatar */}
						</div>
						<LoginForm />
					</Portlet.Body>
				</Portlet>
				{/* END Portlet */}
			</Col>
		</Row>
	)
}

// Form validation schema
const validationSchema = yup.object().shape({
	email: yup.string().email('Your email is not valid').required('Please enter your email'),
	password: yup.string().min(6, 'Please enter at least 6 characters').required('Please provide your password'),
})

const LoginForm: React.FC = (props) => {
	const dispatch = useDispatch();
	const loading = useSelector(getSLoading);
	const { control, handleSubmit, watch } = useForm<LoginFormInputs>({
		resolver: yupResolver(validationSchema),
		defaultValues: {
			email: '',
			password: '',
		},
	})


	// Function to handle form submission
	const onSubmit = async (formData: LoginFormInputs) => {
		// Show loading indicator
		dispatch(AShowLoading());

		try {
			console.log('On submit');
			const payload={email: formData.email, password:formData.password};
			// Try to login with email and password
			// const res = await dispatch(ALoginRequest(payload));
			const res = await postLogin(payload);
			if (res) {
				if (isSuccessRequest(res)) {
					console.log('success', res.data);
					dispatch(ALoginSuccess({token: res.data}));
				} else {
					console.log('Not success, ');
				}
			}

		// 	const redirectUrl = (Router.query.redirect as string) || PAGE.homePagePath
		// 	// Redirect to home page or url from the query parameter
		// 	Router.push(redirectUrl)
		} catch (error: any) {
			swal.fire({ text: error.message, icon: 'error' })
		}
		dispatch(AHideLoading());
	}

	return (
		<Form onSubmit={handleSubmit(onSubmit)} className="d-grid gap-3">
			{/* BEGIN Validation Controller */}
			<Controller
				name="email"
				control={control}
				render={({ field, fieldState: { invalid, error } }) => (
					<Form.Group controlId="email">
						<Form.Floating>
							<Form.Control
								type="email"
								size="lg"
								placeholder="Please insert your email"
								isInvalid={invalid}
								{...field}
							/>
							<Form.Label>Email</Form.Label>
							{invalid && <Form.Control.Feedback type="invalid">{error?.message}</Form.Control.Feedback>}
						</Form.Floating>
					</Form.Group>
				)}
			/>
			{/* END Validation Controller */}
			{/* BEGIN Validation Controller */}
			<Controller
				name="password"
				control={control}
				render={({ field, fieldState: { invalid, error } }) => (
					<Form.Group controlId="password">
						<Form.Floating>
							<Form.Control
								type="password"
								size="lg"
								placeholder="Please insert your password"
								isInvalid={invalid}
								{...field}
							/>
							<Form.Label>Password</Form.Label>
							{invalid && <Form.Control.Feedback type="invalid">{error?.message}</Form.Control.Feedback>}
						</Form.Floating>
					</Form.Group>
				)}
			/>
			{/* END Validation Controller */}
			{/* BEGIN Flex */}
			<div className="d-flex align-items-center justify-content-between">
				<span>
					Don&apos;t have an account? <Link href="/register">Register</Link>
				</span>
				<Button type="submit" variant="label-primary" size="lg" width="widest" disabled={loading}>
					{loading && <Spinner animation="border" size="sm" className="me-2" />}
					Login
				</Button>
			</div>
			{/* END Flex */}
		</Form>
	)
}

interface LoginFormInputs {
	email: string
	password: string
}

LoginPage.pageTitle = 'Login'
LoginPage.layoutName = 'blank'

export default withGuest(LoginPage)
// export default LoginPage
