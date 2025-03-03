from app.models import User, db


def create_user(user_data):
    """새로운 사용자 생성"""
    new_user = User(
        name=user_data['name'],
        age=user_data['age'],
        gender=user_data['gender'],
        email=user_data['email']
    )

    # 이메일 중복 검사
    existing_user = User.query.filter_by(email=new_user.email).first()
    if existing_user:
        return {"ValueError": "이미 존재하는 계정 입니다."}, 409

    db.session.add(new_user)
    db.session.commit()

    return {
        "message": f"{new_user.name}님 회원가입을 축하합니다",
        "user_id": new_user.id
    }, 201


def get_all_users():
    """전체 사용자 목록 조회"""
    users = User.query.all()
    return [user.to_dict() for user in users], 200


def get_user_by_id(user_id):
    """특정 사용자 조회"""
    user = User.query.get_or_404(user_id)
    return user.to_dict(), 200


def update_user(user_id, user_data):
    """사용자 정보 수정"""
    user = User.query.get_or_404(user_id)

    user.name = user_data.get('name', user.name)
    user.email = user_data.get('email', user.email)
    user.gender = user_data.get('gender', user.gender)
    user.age = user_data.get('age', user.age)

    db.session.commit()
    return {"msg": "User updated successfully"}, 200


def delete_user(user_id):
    """사용자 삭제"""
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return {"msg": "User deleted successfully"}, 200
